#!/usr/bin/env python2
# written by Moses Arocha
# This is a port scan that also grabs the application banner of that port

import optparse
from socket import *
from threading import *

ThreadingDisplayLimit = Semaphore(value=1)		# Limits the display of the threading, so only one function is displayed at a time.

def ConnectionScan(TargetHost, TargetPort):
    try: # The attemption to send a SYN packet to create a TCP session.
        ConnectionToSocket = socket(AF_INET, SOCK_STREAM)	
        ConnectionToSocket.connect((TargetHost, TargetPort))
        ConnectionToSocket.send('KaliWithUbuntu\r\n')		
        results = ConnectionToSocket.recv(100)
        ThreadingDisplayLimit.acquire()
        # If the package is successfully received, this tells the port scan it is open.
        print '\n\t[Success] %d/ TCP Port Open'% TargetPort
        print '\n\t[Success] ' + str(results)
    except:
        ThreadingDisplayLimit.acquire()
        print '\t\t[Failure] %d/ TCP Port Closed'% TargetPort   # After the attemption TCP session creation, if it fails, the port is closed.
    finally:
    	# Required, most release the Display screen and close the socket if it was created.
        ThreadingDisplayLimit.release()
        ConnectionToSocket.close()		

def PortScanner(TargetHost, TargetPorts):
    try:
        TargetIP = gethostbyname(TargetHost)			 # Inclusion of a NS that will grab the IP's of URL's, if unknown.
    except:
        print "\n\t[Failure] Cannot resolve '%s': Host Does Not Exist"%TargetHost
        return
    try:
        TargetName = gethostbyaddr(TargetIP)		 	  # Inclusion of reverse NS that will grab the URL's of the IP's 
        print '\n\t[Success] Scan Results for: ' + TargetName[0]  
    except:							  
        print '\n\t[Success] Scan Results for: ' + TargetIP
    setdefaulttimeout(1)					 # If no response is recevied from the port, it will time out to prevent overload.
# The beginning of the threading for each port, it seperates the scans, and displays them individually, to speed up scan.
    for TargetPort in TargetPorts:
        threading = Thread(target=ConnectionScan, args=(TargetHost, int(TargetPort))) # References the ConnectionScan function
        threading.start()

def main():
    extensions = optparse.OptionParser('Uses For Program: '+ '-H <target host> -P <target port>')
    extensions.add_option('-H', '--Host', dest = 'TargetHost', type='string', help = 'Please Write The Exact Host Targeted')
    extensions.add_option('-P', '--Port', dest = 'TargetPort', type='string', help = 'Please Write The Exact Ports, Only Seperated By Comma')
    (options,args) = extensions.parse_args()
    TargetHost = options.TargetHost
    TargetPorts = str(options.TargetPort).split(',')		# The seperation of the ports, that inserts into the list
    if (TargetHost == None) | (TargetPorts[0] == None):  	# The creation of a quick list of all of the Ports, it grabs the first.
        print extensions.usage
        exit(0)
    if not os.geteuid() == 0:
        sys.exit('Must Be Root!')
    PortScanner(TargetHost, TargetPorts)			# The reference to PortScanner function must be last to go through all error handling.

if __name__ == "__main__":
    main()
