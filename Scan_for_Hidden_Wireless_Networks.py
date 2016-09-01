#!/usr/bin/env python2
# written by Moses Arocha
# Created in Python, with the help of TJ O'Connor's book "Violent Python".

import sys
import os
from scapy.all import *

interface = 'mon0'				# Uses the wireless NIC called mon0, must put Network Card in Monitor mode with name of mon0
HiddenNetworks = []
ShownNetworks = []

def SniffNetwork(p):
    if p.haslayer(Dot11ProbeResp):
        MACAddr = p.getlayer(Dot11).addr2					# Grabs the MAC Address of the wireless connection
	if (MACAddr in HiddenNetworks) & (MACAddr not in ShownNetworks):	# Checks to see if MAC Address is in wireless 
	    netName = p.getlayer(Dot11ProbeResp).info
	    print '\t[Success] Decloacked Hidden SSID ' + netName + ' for MAC: ' + MACAddr	
	    ShownNetworks.append(MACAddr)
if p.haslayer(Dot11Beacon): 				# Function that detects the hidden networks Beacon signals
    if p.getlayer(Dot11Beacon).info == '':
        MACAddr = p.getlayer(Dot11).MACAddr
	if MACAddr not in HiddenNetworks:
	    print '\t[Attempt] Detected Hidden SSID with MAC: ' + MACAddr	
	    HiddenNetworks.append(MACAddr)

if not os.geteuid() == 0:
    sys.exit('\t Please Run As Root!!')		# Checks to see if the user is root, this code can only be run in root
os.system('airmon-ng start wlan0')		# Interacts with terminal to put the wireless NIC in monitor mode.
print " \t The Sniffing Has Begun... Please Wait... \n"
sniff(iface=interface, prn=SniffNetwork)	# Must be placed last so monitor mode can be enabled.



