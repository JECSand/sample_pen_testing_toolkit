# sample_pen_testing_toolkit

## Overview

A collection of useful pen testing scripts I wrote in Python. The kit includes a port scanner, an email dictionary attack, and a ssh dictionary attack. This code is strictly for educational/legitimate use only. To help discourage malicious misuse of my code some advanced functionality was left out deliberately. I am 100% against any illegal activities.

## Features
Runs on Linux, Mac and Windows machines.
The scripts are set up to automatically install all unmet prerequisite packages using pip
Tested on Python 2.7 and 3.5

This Kit Includes:
* port_scanner.py:
    * Python script that scans a targeted domain server for open TCP/IP ports and prints them to console
* email_dictionary_attack.py:
    * Dictionary Attack script that attempts to brute force connect to a email's SMTP server using a password list
* ssh_dictionary_attack.py:
    * Another Dictionary Attack script that attempts to brute force a ssh connection with server via a TCP/IP port using a password list
* A set of password list files from https://github.com/berzerk0/Probable-Wordlists:
    * [Password File License](https://github.com/berzerk0/Probable-Wordlists/blob/master/License.txt) - Please review berzerk0's License

## How to Use
1. Make sure you have python 2 or 3 installed with pip on your machine
2. Clone the git repository
```R
git clone https://github.com/JECSand/sample_pen_testing_toolkit.git
```
3. cd into the sample_pen_testing_toolkit directory
4. Instructions on how to run the scripts:
* port_scanner.py:
    * python port_scanner.py "target_domain"
        * target_domain - The parameter which specifies the domain you want to run the port scan on
        * An IP Address would work as well
* email_dictionary_attack.py:
    * python email_dictionary_attack.py "target_email" "desired_password_list" "email_service"(Optional) "target_port_number"(Optional)
        * target_email - Simply the email address the script will run against
        * desired_password_list - Password list (aka dictionary) chosen from the "dictionaries" sub-directory in this repo
        * email_service - Optional Parameter used when the targeted email has a different domain name than the SMPT server it uses. Default is 'gmail.com'
        * target_port_number = Optional Parameter that specifies the port to be targeted by the script. Default is port 587
* ssh_dictionary_attack.py:
    * python ssh_dictionary_attack.py "target_host" "desired_password_list" "user_name" "target_port_number"(Optional)
        * target_host - Simply the domain name or IP Address you wish to run the script on
        * desired_password_list - Password list (aka dictionary) chosen from the "dictionaries" sub-directory in this repo
        * user_name - Name of the user you are trying to login as
        * target_port_number = Optional Parameter that specifies the port to be targeted by the script. Default is port 22

## Examples
1. port_scanner.py:
```R
python3 port_scanner.py "www.domain.com"
```
2. email_dictionary_attack.py:
```R
python email_dictionary_attack.py "notrealtesting@hotmail.com" "Top3575-probable.txt"
```
* (If the user has an email from a different domain that uses the 'smtp.gmail.com' server):
```R
python3 email_dictionary_attack.py "jack@fakeemail.com" "Top3575-probable.txt" "gmail.com" "160"
```
3. ssh_dictionary_attack.py:
```R
python ssh_dictionary_attack.py "domain.com" "Top196-probable.txt" "root" "21"
```

## Disclaimers
1. __From the Author of the Python Scripts__:
___Strictly For Educational/Ethical Pen Testing Purposes ONLY___
I condone no illegal activities with these scripts. If you commit crimes, then you are on your own. You have been forewarned.
Use of this code for unlawful purposes is wrong in every sense of the word, a crime, and I strictly discouraged it.

The intention of this code is to give legitimate users a better understanding on how to protect their own personal email accounts and servers.
I'd encourage everyone who comes across this to only use solid random passwords not containing any words and to be safe online.
To help discourage/limit illegal use of this code, advanced functionality of these scripts has been removed/limited
All password list dictionary files provided in this repo were 100% legally created and include their own license/disclaimer

2. __From the Author of the Password Files__:
___These lists are for LAWFUL, ETHICAL AND EDUCATIONAL PURPOSES ONLY___.
The files contained in this repository are released "as is" without warranty, support, or guarantee of effectiveness.
However, I am open to hearing about any issues found within these files and will be actively maintaining this repository for the foreseeable future. If you find anything noteworthy, let me know and I'll see what I can do about it.

The author did not steal, phish, deceive or hack in any way to get hold of these passwords. All lines in these files were obtained through freely available means.

The author's intent for this project is to provide information on insecure passwords in order to increase overall password security. The lists will show you what passwords are the most common, what patterns are the most common, and what you should avoid when making them.
