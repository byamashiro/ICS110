import xml.etree.ElementTree as ET

with open('catalog.xml', 'rb') as data:
	xmlParsed = ET.parse(data)

elemList = set()

for elem in xmlParsed.iter():
	elemList.add(elem.tag)

for elem in xmlParsed.iter('price'):
	price = float(elem.text)
	new_price = round((price * 1.15), 2)
	elem.text = str(new_price)
	print(elem.text)

xmlParsed.write('my_xml_02_output.xml')
