# Python Code

Every single Python file in this repository is independent of each other, unless specified in the comments. 
Every file is an independent tool that can aid in network monitoring or analysis.

Thank you TJ O'Connor.
 
(Suggestion. Run all code as Super-user or Administrator)

Please install dpkt and GeoLiteCity packets
Run the following commands:

  $ sudo apt-get install python-dpkt
  
  $ wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
  
  $ gunzip GeoLiteCity.dat.gz
  
  $ mkdir /opt/GeoIP
  
  $ mv GeoLiteCity.dat /opt/GeoIP/Geo.dat
  
  $ sudo apt-get install python-nmap
  
  $ sudo apt-get install python-scapy
  
  $ sudo apt-get install xprobe2
