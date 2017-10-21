# Connor Sanders
# 10/15/2017
# Tested and Developed on Python 2.7 and 3.5 / Configured for Windows, Linux, and Mac

# Strictly For Educational/Ethical Pen Testing Purposes ONLY. I condone no illegal activities with this script
# Use of this code for unlawful purposes is wrong in every sense of the word, a crime, and strictly discouraged
# To help discourage/limit illegal use of this code, advanced functionality of the script has been removed/limited
# All sample dictionary files provided in this repo were 100% legally created and include their own license/disclaimer

# How to use the code:
#   python3 port_scanner.py tar_host

#   Usage examples:
#     python3 port_scanner.py www.domain.com

import sys
import subprocess
from datetime import datetime
from socket import *

# Script Variables
tar_host = ''
print(sys.version_info[0])
if sys.version_info[0] == 3:
    py_version = '3'
else:
    py_version = '2'
max_port_num = 5000
min_port_num = 1
subprocess.call('clear', shell=True)


# Function to scan a specific port belonging to the targeted host
def scan_tar(tar_host, port_num):
    return_code = 1
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        re_code = sock.connect_ex((tar_host, port_num))
        if re_code == 0:
            return_code = re_code
        sock.close()
    except KeyboardInterrupt:
        print("[!]------> Exited Script on User's Request!")
        sys.exit(1)
    except socket.gaierror:
        print('[!]------> Hostname Problem. Exiting Now...')
        sys.exit(1)
    except socket.error:
        print("[!]------> Couldn't connect to targeted server. Exiting Now...")
        sys.exit(1)
    except Exception:
        pass
    return return_code


# Main Function to run script
def main(tar_host):
    s_time = datetime.now()
    tar_ip = gethostbyname(tar_host)
    print('[#]----> Targeted HOST: ' + tar_host + '\n' + '[#]----> Targeted IP: ' + tar_ip)
    print('[#]----> Scanning in Progress....\n[#]------> This may take awhile...')
    if py_version == '3':
        port_range = range(min_port_num, max_port_num)
    elif py_version == '2':
        port_range = list(range(min_port_num, max_port_num))
    else:
        print('[!]------> Unrecognized python version! Exiting....')
        sys.exit(1)
    for try_port_num in port_range:
        try:
            res = scan_tar(tar_ip, try_port_num)
            if res == 0:
                print("[*]--------> Port " + str(try_port_num) + ": Open")
        except Exception:
            pass
    e_time = datetime.now()
    run_time = e_time - s_time
    print('[#]----> Port Scan of ' + tar_host + ' | ' + tar_ip + ' is complete!')
    print('\n[#]------> Scan Total Run Time: ' + str(run_time))


if __name__ == "__main__":
    main(sys.argv[1])
