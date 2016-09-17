#!/usr/bin/env python2
# written by Moses Arocha
# This code was written with the assist of TJ O'Connor's "Violent Python"

import os
import nmap
import optparse

def PortScan(TargetHost, TargetPort):		
    NmapScan = nmap.PortScanner()				# Creates a specific type of scanner from the nmap library, this one is a port scanner
    NmapScan.scan(TargetHost, TargetPort)			# This function grabs the library, then tells it that it is going to use the TargetHost and TargetPort variables
    state = NmapScan[TargetHost]['tcp'][int(TargetPort)]['state']
    print "\n [Results] " + TargetHost + " TCP Port/" +TargetPort + " " + state	
    # The output the user finally sees, displays if the host, and which ports are open

# The main function grabs the users input, analyzes it to make sure it is valid, then sends the information to the PortScan function #
def main():
    extensions = optparse.OptionParser('Uses For Program: -H <Target Host> -P <Target Port>')
    extensions.add_option('-H', '--Host', dest='TargetHost', type='string', help='specify target host')
    extensions.add_option('-P', '--Port',  dest='TargetPort', type='string', help='specify targe port')
    (options, args) = extensions.parse_args()		
    TargetHost = options.TargetHost			
    TargetPorts = str(options.TargetPort).split(',')
    if (TargetHost == None) | (TargetPorts[0] == None):		
        print extensions.usage
	exit(0)							
    if not os.geteuid() == 0:
    	sys.exit('Must Be Root!')				# Checks to see if UID 0 is enabled, only works for LINUX, not Windows
    for TargetPort in TargetPorts:
	PortScan(TargetHost, TargetPort)			# Call for PortScan function must be at end to go through all error handling

if __name__ == '__main__':
    main()
