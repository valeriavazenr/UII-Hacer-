import xml.etree.cElementTree as et

root = et.Element("UTC.xml")

se = et.SubElement(root,"Alumnos1.1")
et.SubElement(se, "Matricula").text = "18040106"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes"
et.SubElement(se, "Nombre").text = "Valeria_Vazquez_Enriquez"

se = et.SubElement(root,"Alumnos1.2")
et.SubElement(se, "Matricula").text = "18040112"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes"
et.SubElement(se, "Nombre").text = "Victoria_Davila_Duran"

se = et.SubElement(root,"Alumnos1.3")
et.SubElement(se, "Matricula").text = "18040109"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes"
et.SubElement(se, "Nombre").text = "Rosa_Rodriguez_Uribe"

se = et.SubElement(root,"Alumnos1.4")
et.SubElement(se, "Matricula").text = "18040110"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes"
et.SubElement(se, "Nombre").text = "Aylin_Arreozola_Sanchez"

se = et.SubElement(root,"Alumnos1.5")
et.SubElement(se, "Matricula").text = "18040111"
et.SubElement(se, "Carrera").text = "Infraestructura_de_Redes"
et.SubElement(se, "Nombre").text = "Jonathan_Hernandez_Hernandez"

se = et.SubElement(root,"Alumnos1.6")
et.SubElement(se, "Matricula").text = "18040113"
et.SubElement(se, "Carrera").text = "Desarollo_de_Software"
et.SubElement(se, "Nombre").text = "Daniel_ALmaguer_Lopez"

se = et.SubElement(root,"Alumnos1.7")
et.SubElement(se, "Matricula").text = "18040105"
et.SubElement(se, "Carrera").text = "Desarollo_de_Software"
et.SubElement(se, "Nombre").text = "Estefania_Mendez_Castro"

se = et.SubElement(root,"Alumnos1.8")
et.SubElement(se, "Matricula").text = "18040115"
et.SubElement(se, "Carrera").text = "Desarollo_de_Software"
et.SubElement(se, "Nombre").text = "Margarita_Perales_Gonzales"

se = et.SubElement(root,"Alumnos1.9")
et.SubElement(se, "Matricula").text = "18040116"
et.SubElement(se, "Carrera").text = "Desarollo_de_Software"
et.SubElement(se, "Nombre").text = "Alejandro_Solano_Dominguez"

se = et.SubElement(root,"Alumnos1.10")
et.SubElement(se, "Matricula").text = "18040117"
et.SubElement(se, "Carrera").text = "Desarollo_de_Software"
et.SubElement(se, "Nombre").text = "Sofia_Esquivel_Enriquez"

se = et.SubElement(root,"Alumnos1.11")
et.SubElement(se, "Matricula").text = "18040106"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales"
et.SubElement(se, "Nombre").text = "Kevin_Cruz_Garcia"

se = et.SubElement(root,"Alumnos1.12")
et.SubElement(se, "Matricula").text = "18040106"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales"
et.SubElement(se, "Nombre").text = "Andrea_Rocha_Ruiz"

se = et.SubElement(root,"Alumnos1.13")
et.SubElement(se, "Matricula").text = "18040106"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales"
et.SubElement(se, "Nombre").text = "Felipe_Gomez_Delgado"

se = et.SubElement(root,"Alumnos1.14")
et.SubElement(se, "Matricula").text = "18040106"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales"
et.SubElement(se, "Nombre").text = "Daniela_Lopez_Rodiguez"

se = et.SubElement(root,"Alumnos1.15")
et.SubElement(se, "Matricula").text = "18040106"
et.SubElement(se, "Carrera").text = "Entornos_Virtuales"
et.SubElement(se, "Nombre").text = "Adolfo_Aranda_Reyna"


tree = et.ElementTree(root)
tree.write("Utc.xml", xml_declaration=True)
