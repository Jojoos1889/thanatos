import os
import socket
banner = '''
████████╗██╗░░██╗░█████╗░███╗░░██╗░█████╗░████████╗░█████╗░░██████╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░███████║███████║██╔██╗██║███████║░░░██║░░░██║░░██║╚█████╗░
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔══██║░░░██║░░░██║░░██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░░██║░░░██║░░░╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═════╝░
''' 
target = input('target-->')
print(banner)
nmap = "nmap -T4 -Pn -v3 -A "+target
testssl = "testssl -9 "+target
nikto = "nikto --host "+target 
host = "host "+target
os.system(nmap)
os.system(testssl)
os.system(nikto)
os.system(host)
print("[+]scan status: 100% Done...")
print("[*]exploitting status: 0% Done...")
os.system("python exploit.py")
print("[+]system violated")
print("[+]creating a remote shell payload")
