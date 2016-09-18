#!/usr/bin/python
# Written by Moses Arocha
#  Created in Python, with the help of TJ O'Connor's book "Violent Python"

from scapy.all import *

import os
import sys
import optparse

PIP = 'TCP'
NAV_PORT = 80
Interface = 'mon0'

def printPkt(pkt):
    global PIP, NAV_PORT
    if pkt.haslayer(PIP) and pkt.getlayer(PIP).dport == NAV_PORT:
        raw = pkt.sprintf('%Raw.load%')
	ip_src = pkt.getlayer(IP).src
	ip_dst = pkt.getlayer(IP).dst
	print '\t IP Source: ' +ip_src +  " \t IP Destination: " + ip_dst + " Raw Packet: " + raw


def main():
     if not os.geteuid() == 0:
        sys.exit('\t Please Run As Root!!')		# Makes sure that UID 0 is enabled.
    parser = optparse.OptionParser("Usages For Program: -I <Interface> -P <Port> --TCP <IP Protocol>")
    parser.add_option('-I', dest ='interface', type='string', help='Specify Interface Type')
    parser.add_option('-P', dest='port', type='int', help='Specify Port Number')
    parser.add_option('--IP', '--IP', dest='InternetProtocol', type='string', help='Specify Internet Protocol')
    (options, args) = parser.parse_args()
    PIP = options.InternetProtocol
    NAV_PORT = options.port
    Interface = options.interface
    os.system('sudo airmon-ng start wlan0')		# Interacts with terminal to put the wireless NIC in monitor mode
    print " \t The Sniffing Has Begun... Please Wait... \n\n"
    if options.interface == None:
	print parser.usage
	exit(0)
    print "Scanning The Network On Port: ", NAV_PORT, "/", PIP, " On Interface: ", Interface
    sniff(prn=printPkt, iface=Interface)


if __name__ == '__main__':
    main()
