#!/usr/bin/env python2
# written by Moses Arocha
# This is a port scan that also grabs the application banner of that port


from threading import *

import optparse
import socket
import sys
import os

ThreadingDisplayLimit = Semaphore(value=1)		# Limits the display of the threading, so only one function is displayed at a time.

def ConnectionScan(Target_Host, Target_Port):
    try: # The attemption to send a SYN packet to create a TCP session.
        ConnectionToSocket = socket(AF_INET, SOCK_STREAM)	
        ConnectionToSocket.connect((Target_Host, Target_Port))
        ConnectionToSocket.send('KaliWithUbuntu\r\n')		
        results = ConnectionToSocket.recv(100)
        ThreadingDisplayLimit.acquire()
        # If the package is successfully received, this tells the port scan it is open.
        print '\n\t[Success] %d/ TCP Port Open'% Target_Port
        print '\n\t[Success] ' + str(results)
    except:
        ThreadingDisplayLimit.acquire()
        print '\t\t[Failure] %d/ TCP Port Closed'% Target_Port   # After the attemption TCP session creation, if it fails, the port is closed.
    finally:
    	# Required, most release the Display screen and close the socket if it was created.
        ThreadingDisplayLimit.release()
        ConnectionToSocket.close()		

def PortScanner(Target_Host, Target_Ports):
    try:
        Target_IP = gethostbyname(Target_Host)			 # Inclusion of a NS that will grab the IP's of URL's, if unknown.
    except:
        print "\n\t[Failure] Cannot resolve '%s': Host Does Not Exist"% Target_Host
        return
    try:
        Target_Name = gethostbyaddr(Target_IP)		 	  # Inclusion of reverse NS that will grab the URL's of the IP's 
        print '\n\t[Success] Scan Results for: ' + Target_Name[0]  
    except:							  
        print '\n\t[Success] Scan Results for: ' + Target_IP
    setdefaulttimeout(1)					 # If no response is recevied from the port, it will time out to prevent overload.
# The beginning of the threading for each port, it seperates the scans, and displays them individually, to speed up scan.
    for Target_Port in Target_Ports:
        threading = Thread(target=ConnectionScan, args=(Target_Host, int(Target_Port))) # References the ConnectionScan function
        threading.start()

def main():
    extensions = optparse.OptionParser('Uses For Program: '+ '-H <target host> -P <target port>')
    extensions.add_option('-H', '--Host', dest = 'TargetHost', type='string', help = 'Please Write The Exact Host Targeted')
    extensions.add_option('-P', '--Port', dest = 'TargetPort', type='string', help = 'Please Write The Exact Ports, Only Seperated By Comma')
    (options,args) = extensions.parse_args()
    Target_Host = options.TargetHost
    Target_Ports = str(options.TargetPort).split(',')		# The seperation of the ports, that inserts into the list
    if (Target_Host == None) | (Target_Ports[0] == None):  	# The creation of a quick list of all of the Ports, it grabs the first.
        print extensions.usage
        exit(0)
    if not os.geteuid() == 0:
        sys.exit('Must Be Root!')
    PortScanner(Target_Host, Target_Ports)			# The reference to PortScanner function must be last to go through all error handling.

if __name__ == "__main__":
    main()
