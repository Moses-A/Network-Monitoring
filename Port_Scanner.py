#!/usr/bin/env python2
# written by Moses Arocha
# This is a port scan that also grabs the application banner of that port

import optparse
from socket import *
from threading import *

ThreadingDisplayLimit = Semaphore(value=1)			# Limits the display of the threading, so it is not all messy when displayed

##The beginning of the ConnectionScan function that attempts to create the sockets and send the SYN packet##
def ConnectionScan(TargetHost, TargetPort):
   try:
	ConnectionToSocket = socket(AF_INET, SOCK_STREAM)	# The attemption to send a SYN packet to create a session
	ConnectionToSocket.connect((TargetHost, TargetPort))	# If the package is successfully received, this tells the port scan it is open
	ConnectionToSocket.send('KaliWithUbuntu\r\n')		
	results = ConnectionToSocket.recv(100)
	ThreadingDisplayLimit.acquire()
	print '\n\t[Success] %d/ TCP Port Open'% TargetPort
	print '\n\t[Success] ' + str(results)
   except:
	ThreadingDisplayLimit.acquire()
	print '\t\t[Failure] %d/ TCP Port Closed'% TargetPort	# Will attempt to make a connection through socket, if fails, port is closed
   finally:
	ThreadingDisplayLimit.release()
	ConnectionToSocket.close()

##The beginning of the PortScanner Function, that alters the data inputed by the user, along with the threading ##
def PortScanner(TargetHost, TargetPorts):
   try:
	TargetIP = gethostbyname(TargetHost)			# Inclusion of a NS that will grab the IP's of URL's
   except:
	print "\n\t[Failure] Cannot resolve '%s': Host Does Not Exist"%TargetHost
	return
   try:
	TargetName = gethostbyaddr(TargetIP)			# Inclusion of reverse NS that will grab the URL's of the IP's 
	print '\n\t[Success] Scan Results for: ' + TargetName[0] # Will attempt to display the IP Address of the URL, depending on what you
   except:							 # insert as the host input
	print '\n\t[Success] Scan Results for: ' + TargetIP
   setdefaulttimeout(1)						 # if no response is recevied from the port, it will time out
   # The beginning of the threading, for each port, it seperates the scans, and displays them individually, to speed up scan
   for TargetPort in TargetPorts:
	threading = Thread(target=ConnectionScan, args=(TargetHost, int(TargetPort))) # reference to the ConnectionScan function
	threading.start()

##The beginning of the main function, the origins of the extensions (optparse) begins here##
def main():
   extensions = optparse.OptionParser('Uses For Program: '+ '-H <target host> -P <target port>')
   extensions.add_option('-H', '--Host', dest = 'TargetHost', type='string', help = 'Please Write The Exact Host Targeted')
   extensions.add_option('-P', '--Port', dest = 'TargetPort', type='string', help = 'Please Write The Exact Ports, Only Seperated By Comma')
   (options,args) = extensions.parse_args()
   TargetHost = options.TargetHost
   TargetPorts = str(options.TargetPort).split(',')		# The seperation of the ports, that inserts into the list
   if (TargetHost == None) | (TargetPorts[0] == None):  	# The creation of a quick list of all of the Ports, it grabs the first in the 
	print extensions.usage
	exit(0)
   if not os.geteuid() == 0:
    	sys.exit('Must Be Root!')
   PortScanner(TargetHost, TargetPorts)				# The reference to PortScanner function, that actually does the scan

if __name__ == "__main__":
	main()