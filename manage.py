import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from libro import Libro

class Manager():
    def __init__(self):
        self.libros = []

    def addLibro(self, id, titulo, autor, idioma, categoria, editorial, copias):
        libro = Libro(id, titulo, autor, idioma, categoria, editorial, copias)
        self.libros.append(libro)
    
    def getLibro(self):
        json = []
        for libro in self.libros:
            libro = {
                'id': libro.id,
                'titulo': libro.titulo,
                'autor': libro.autor,
                'idioma': libro.idioma,
                'categoria': libro.categoria,
                'editorial': libro.editorial,
                'copias': libro.copias
            }
            json.append(libro)
        return json
    
    def getLibroId(self, id):
        for libro in self.libros:
            if libro.id == id:
                return libro
        return None
    
    def getLibrosCategoria(self, categoria):
        libros_categoria = [libro for libro in self.libros if libro.categoria == categoria]
        json = []
        for libro in libros_categoria:
            libro_json = {
                'id': libro.id,
                'titulo': libro.titulo,
                'autor': libro.autor,
                'idioma': libro.idioma,
                'categoria': libro.categoria,
                'editorial': libro.editorial,
                'copias': libro.copias
            }
            json.append(libro_json)
        return json


    def createXMLFromID(self, id):
        for libro in self.libros:
            if libro.id == id:
                root = ET.Element('libro', attrib={'id': libro.id})
                ET.SubElement(root, 'titulo').text = libro.titulo
                ET.SubElement(root, 'autor').text = libro.autor
                ET.SubElement(root, 'idioma').text = libro.idioma
                ET.SubElement(root, 'categoria').text = libro.categoria
                ET.SubElement(root, 'editorial').text = libro.editorial
                ET.SubElement(root, 'copias').text = str(libro.copias)
                
                tree = ET.ElementTree(root)
                xml_str = ET.tostring(root, encoding='utf-8')
                pretty_xml_str = parseString(xml_str).toprettyxml(indent="  ", encoding='utf-8')
                
                return pretty_xml_str.decode('utf-8')
        return None