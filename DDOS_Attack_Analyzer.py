#!/usr/bin/env python2
# written by Moses Arocha
# Written with the help of TJ O'Connor in his book "Violent Python"

import dpkt
import socket
import optparse

THRESH = 1000

def DDOSAttack(pcap):				
    packet_Count = {}					# Begins the packet Counting at null or zero
        for (ts, buf) in pcap:				# Grabs the PCAP file for network monitoring
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                source = socket.inet_ntoa(ip.src)	# Within the PCAP file grabs the source IP address
                destination = socket.inet_ntoa(ip.dst)	# Within the PCAP file grabs the destination IP address
                tcp = ip.data
                Destination_Port = tcp.Destination_Port	# Grabs the destination port from the TCP data anaylzed in the PCAP file
                if Destination_Port == 80 or Destination_Port == 443:	# If the Destination port is either 80 or 443 it continues
                    stream = source + ':' + destination
                    if packet_Count.has_key(stream):			
                        packet_Count[stream] = packet_Count[stream] + 1
                    else:
    	                packet_Count[stream] = 1
            except:
		pass

    for stream in packet_Count:
        packets_Sent = packet_Count[stream]
        if packets_Sent > THRESH:
            source = stream.split(':')[0]
            destination = stream.split(':')[1]
            print '[+] ' +source+ ' attacked '+destination+ 'with ' + str(packets_Sent) + 'pkts.'	
            # The only output the user will see, only seen if an attack is occuring by the packets sent from an IP Address exceeds the thresh hold amount

# The main will examine the user's input, open up the pcap file, then will forward the information to the DDOSAttack function #
def main():
    if not os.geteuid() == 0:
        sys.exit('Must Be Root!')				# This code checks to see if a user is root
    parser = optparse.OptionParser("Usages For Program:  -r <Read PCAP File> -t <Thresh Holder>")
    parser.add_option('-r', '--Read', dest ='pcapFile', type='string', help='specify pcap filename')
    parser.add_option('-T', '--Thresh', dest='thresh', type='int', help='specify threshold count')
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print parser.usage					# The catch all function for the parser
        exit(0)			
    if parser.thresh != None:					# If the user doesn't enter in an interger for the thresh, it automatically defaults to the set global value of 1000
	THRESH = parser.thresh
    pcap_File = parser.pcapFile
    f = open(pcap_File)					
    pcap = dpkt.pcap.Reader(f)					# Analyzes the pcap and sends the information along
    DDOSAttack(pcap)						# Calls for the DDOSAttack function

if __name__ == '__main__':
    main()
