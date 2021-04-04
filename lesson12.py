import socket
import sys

def lookup(addr):
     try:
         return socket.gethostbyaddr(addr)
     except socket.herror:
	  return None, None, None


localMachine = socket.gethostname()
IPGoogle = socket.gethostbyname("www.google.com")
computerName = lookup("172.18.63.194")

print("The name of local machine: {}".format(localMachine))
print("IP Adress of Google: {}".format(IPGoogle))
print("The name of local machine: {}".format(computerName))
