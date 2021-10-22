import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file = parse('UTC.xml')

root = et.Element("Alumnos")

xmlRoot = xml_file.getroot()



se = et.SubElement(root,"Alumnos1.16")
et.SubElement(se, "Matricula").text = "1805892"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes"
et.SubElement(se, "Nombre").text = "Sugey_Davila_Ramirez"
xmlRoot.append(se)


xml_file.write("Alumnos1.xml",xml_declaration=True)
