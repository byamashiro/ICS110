import xml.etree.ElementTree as ET

with open('catalog.xml', 'rb') as data:
	xmlParsed = ET.parse(data)

elemList = set()

for elem in xmlParsed.iter():
	elemList.add(elem.tag)


increase = float(input('Enter the price increase: '))

for elem in xmlParsed.iter('price'):
	price = float(elem.text)
	new_price = round((price * increase), 2)
	elem.text = str(new_price)
	print(elem.text)

xmlParsed.write('my_xml_03_output.xml')

