#!/usr/bin/python
# Written by Moses Arocha
#  Created in Python, with the help of TJ O'Connor's book "Violent Python"

from scapy.all import *
import os
import optparse

PIP = 'TCP'
NAVPORT = 80
Interface = 'mon0'

def printPkt(pkt):
    global PIP, NAVPORT
    if pkt.haslayer(PIP) and pkt.getlayer(PIP).dport == NAVPORT:
        raw = pkt.sprintf('%Raw.load%')
	ipsrc = pkt.getlayer(IP).src
	ipdst = pkt.getlayer(IP).dst
	print '\t IP Source: ' +ipsrc +  " \t IP Destination: " + ipdst + " Raw Packet: " + raw


def main():
    parser = optparse.OptionParser("Usages For Program: -I <Interface> -P <Port> --TCP <IP Protocol>")
    parser.add_option('-I', dest ='interface', type='string', help='Specify Interface Type')
    parser.add_option('-P', dest='port', type='int', help='Specify Port Number')
    parser.add_option('--IP', '--IP', dest='InternetProtocol', type='string', help='Specify Internet Protocol')
    (options, args) = parser.parse_args()
    PIP = options.InternetProtocol
    NAVPORT = options.port
    Interface = options.interface
    if not os.geteuid() == 0:
        sys.exit('\t Please Run As Root!!')		# Makes sure that UID 0 is enabled.
    os.system('sudo airmon-ng start wlan0')		# Interacts with terminal to put the wireless NIC in monitor mode
    print " \t The Sniffing Has Begun... Please Wait... \n\n"
    if options.interface == None:
	print parser.usage
	exit(0)
    print "Scanning The Network On Port: ", NAVPORT, "/", PIP, " On Interface: ", Interface
    sniff(prn=printPkt, iface=Interface)


if __name__ == '__main__':
    main()
