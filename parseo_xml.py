import xml.etree.ElementTree as ET
tree = ET.parse('O365IPAddresses.xml')
root = tree.getroot()

for address in root[18][0].iter('address'):
    print(address.text)


"""Pequeño script para extraer datos de una determinada etiqueta, en este caso, la  
   número 19. Sirve sólo para archivo XML con datos estáticos"""
