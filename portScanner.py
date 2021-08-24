import sys
import socket
from datetime import datetime as dt

def newLine() :
	print("\n")


#No threading...

#Define our target
if (len(sys.argv) == 2):
	target = socket.gethostbyname(sys.argv[1]) #Trans hostname to IPV4
else:
	print("Invalid number of args")
	print("Syntax: python3 portScanner.py <ip>")
	sys.exit()

#Add a pretty banner
print("-"*50)
print("Scanning target: "+target)
print("Time started: "+ str(dt.now()))
print("-"*50)

try: 
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4;SOCK_STREAM = port
		socket.setdefaulttimeout(1) #is a float
		print("Scanning port {}".format(port))
		result = s.connect_ex((target, port))
		if (result == 0):
			print("Port {} is open.".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("\nHostname could not be resolved.")
	sys.exit()
except socket.error:
	print("\nServer is down")
	sys.exit()