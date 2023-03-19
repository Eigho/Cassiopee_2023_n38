import xml.etree.ElementTree as ET
import csv

def importXmlToCsvAndSum():
	consototale=0
	with open('chicane_emission.csv', 'w', newline='') as g:
		writer=csv.writer(g)
		f=open("chicane_out.xml","r")
		contents = f.read()
		xml = ET.fromstring(contents)

		for timestep in xml:
			for vehicle in timestep:
				fuel=float(vehicle.attrib['CO2'])
				#if (fuel==0):
				#	fuel=0.2778
				consototale+=fuel
				writer.writerow([vehicle.attrib['id'],vehicle.attrib['CO2']])
	return(consototale)

print("Test : ", importXmlToCsvAndSum())