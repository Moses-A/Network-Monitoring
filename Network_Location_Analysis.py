#!/usr/bin/env python2
#Author is Moses Arocha
# Created in Python, created with the help of TJ O'Connor "Violent Python"

import os
import sys
import dpkt
import socket
import pygeoip
import optparse

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')	#Inclusion of Geo.dat database which allows for the location of all IP's

#Analyzes the IP's to discover the location of origination#
def retrieveGeographicSource(ip):		
    try:
        rec = gi.record_by_name(ip)
        city =  rec['city']			# The inclusion of the city, country based on the IP address
        if city != '':					
            Location = city + ', ' + country
        else:
            Location = country				
        return Location
    except Exception, e:
        return 'Unfound'			# Program does not check for spoofed IP, registers as Unfound

#Analyzes the PCAP file, organizes it, then prints out the Source and Destination, IP Address and location#
def AnalyzePcap(pcap):				
    for (ts, buf) in pcap:				
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            source = socket.inet_ntoa(ip.src)						# retrieves the source IP address from PCAP file
            destination = socket.inet_ntoa(ip.dst)					# retrieves the destination IP address from PCAP file
            # The only two lines that the user will ever see
            print ' Source IP : ' + source + '--> Destination IP: ' + destination
            print 'Source IP Location: ' + retrieveGeographicSource(source) + '--> Destination IP Location: ' + retrieveGeographicSource(destination)
        except:
            pass

# The beginning of the main, grabs the user's input for which pcap file to analyze #
def main():
    parser = optparse.OptionParser('Usages For Program: -r <pcap file>')	# The inclusiong of the optparse 
    parser.add_option('-r', '--Read', dest='pcapFile', type='string', help='specify pcap filename')
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print parser.usage
        exit(0)
    if not os.geteuid() == 0:
        sys.exit('Must Be Root!')	# Checks to see if a user is root, checks UID 0 in Linux, does NOT work for Windows
    pcapFile = options.pcapFile
    f = open(pcapFile)					
    pcap = dpkt.pcap.Reader(f)					
    AnalyzePcap(pcap)			# Must be at end of line for all error handling to occur

if __name__ == '__main__':
    main()
