

import socket
from termcolor import colored
import pyfiglet

bannar = colored(pyfiglet.figlet_format("IP FINDER"),'blue')
print(bannar)

domain= input("Enter your URL: ")

ip = socket.gethostbyname(domain)

print(ip)
