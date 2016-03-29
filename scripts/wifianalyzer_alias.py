import os
import sys
import json
import urllib2
import time


json_data = urllib2.urlopen('') #nodes.json
data = json.load(json_data)
linesdone = 0
filename="WifiAnalyzer_Alias.txt" #filename for output file

if os.path.exists(filename):
	try:
		os.remove(filename)
	except OSError, e:
		print ("Error: %s - %s." % (e.filename,e.strerror))
		
file = open(filename,"a")
file.write('#WifiAnalyzer Alias-Include Freifunk Wiesbaden\n')
file.write('#Generated on ' + time.strftime("%A, %d.%m.%Y %H:%M:%S") + '\n\n')
file.close()

for x in data["nodes"]: 
	#foking 5GHz nodes
	if x["nodeinfo"]["hardware"]["model"] in ['TP-Link TL-WDR3600 v1', 'TP-Link TL-WDR4300 v1', 'TP-Link TL-WDR3500 v1', 'TP-Link Archer C5 v1', 'TP-Link Archer C7 v2', 'TP-Link CPE510 v1.0']:
		
		mac = x["nodeinfo"]["network"]["mac"]
	
		wifi1_mac = str(mac).split(':')
		wifi1_mac[0] = int(wifi1_mac[0], 16) + 2
		wifi1_mac[1] = int(wifi1_mac[1], 16) + 2
		if (wifi1_mac[1] >= 0x100):
			wifi1_mac[1] = 0
		wifi1_mac[2] = int(wifi1_mac[2], 16) + 2
		if (wifi1_mac[2] >= 0x100):
			wifi1_mac[2] = 0
		wifi1_mac[3] = int(wifi1_mac[3], 16)
		wifi1_mac[4] = int(wifi1_mac[4], 16)
		wifi1_mac[5] = int(wifi1_mac[5], 16)
		wifi1_mac_str = ':'.join('%02x'%i for i in wifi1_mac)
	
		hostname = x["nodeinfo"]["hostname"]
		result1 = wifi1_mac_str +"|"+ hostname + "_5GHz"
		print(result1)
		FinalData = open(filename, "a")
		FinalData.write(result1 + '\n')
		linesdone = linesdone + 1
	

	
	mac = x["nodeinfo"]["network"]["mac"]
	
	wifi0_mac = str(mac).split(':')
	wifi0_mac[0] = int(wifi0_mac[0], 16) + 2
	wifi0_mac[1] = int(wifi0_mac[1], 16) + 2
	if (wifi0_mac[1] >= 0x100):
		wifi0_mac[1] = 0
	wifi0_mac[2] = int(wifi0_mac[2], 16) + 1
	if (wifi0_mac[2] >= 0x100):
		wifi0_mac[2] = 0
	wifi0_mac[3] = int(wifi0_mac[3], 16)
	wifi0_mac[4] = int(wifi0_mac[4], 16)
	wifi0_mac[5] = int(wifi0_mac[5], 16)
	wifi0_mac_str = ':'.join('%02x'%i for i in wifi0_mac)
	
	
	hostname = x["nodeinfo"]["hostname"]
	result0 = wifi0_mac_str +"|"+ hostname
	print(result0)
	FinalData = open(filename, "a")
	FinalData.write(result0 + '\n')
	linesdone = linesdone + 1
	
print('')
print('#Processed ' +str(linesdone) + ' lines')