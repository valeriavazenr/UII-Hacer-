from xml.etree.ElementTree import parse, Element

file_name = 'Alumnos1.xml'
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find('Alumnos1.15'))

new_file = 'Reg.xml'
doc_xml.write(new_file, xml_declaration=True)
