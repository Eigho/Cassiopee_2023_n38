import xml.etree.ElementTree as ET
import csv

def importXmlToCsvAndSum():
	consototale=0
	with open('test.csv', 'w', newline='') as g:
		writer=csv.writer(g)
		f=open("test.xml","r")
		contents = f.read()
		xml = ET.fromstring(contents)

		for timestep in xml:
			for vehicle in timestep:
				fuel=float(vehicle.attrib['CO2'])
				#if (fuel==0):
				#	fuel=0.2778
				consototale+=fuel
				writer.writerow([timestep.attrib['time'],vehicle.attrib['speed'],vehicle.attrib['CO2']])
	return(consototale)

print("Test : ", importXmlToCsvAndSum())