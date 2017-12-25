#!/usr/bin/python
from scapy.all import *

for i in range(60,80,2):
	for a in range(10,110,10):
		pkt = IP(src="192.168.242."+str(a),dst="192.168.242.172")/TCP(sport=i,flags="S")
		send(pkt)
