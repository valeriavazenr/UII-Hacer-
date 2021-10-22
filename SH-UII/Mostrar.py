from xml.etree import ElementTree
import pprint

with open('Alumnos1.xml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter():
       print(node.tag)
       print(node.text)
