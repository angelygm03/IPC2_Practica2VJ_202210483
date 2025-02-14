from flask import Flask, request, jsonify
from xml.etree import ElementTree as ET
from manage import Manager

app = Flask(__name__)
manager = Manager()

@app.route('/')
def index():
    return "API con Python y Flask funcionando correctamente"

@app.route('/cargarLibros', methods=['POST'])
def cargarLibros():
    xml = request.data.decode('utf-8')
    raiz = ET.XML(xml)
    
    for elemento in raiz:
        id = elemento.attrib.get('id')
        titulo = elemento.find('titulo').text
        autor = elemento.find('autor').text
        idioma = elemento.find('idioma').text
        categoria = elemento.find('categoria').text
        editorial = elemento.find('editorial').text
        copias = int(elemento.find('copias').text)

        manager.addLibro(id, titulo, autor, idioma, categoria, editorial, copias)

    return jsonify({"message": "Archivo XML cargado correctamente"}), 200

@app.route('/verLibros', methods=['GET'])
def verLibros():
    libros = manager.getLibro()
    return jsonify(libros), 200

@app.route('/verLibro/:<id>', methods=['GET'])
def crearXML(id):
    xml_str = manager.createXMLFromID(id)
    if xml_str:
        return xml_str, 200, {'Content-Type': 'application/xml'}
    else:
        return jsonify({"message": "Libro no encontrado"}), 404


@app.route('/libros/:<categoria>', methods=['GET'])
def verLibroCategoria(categoria):
    libros = manager.getLibrosCategoria(categoria)
    if not libros:
        return jsonify({"message": "Libros no encontrados"}), 404
    return jsonify(libros), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
