from manage import Manager
from flask import Flask, request, jsonify
from xml.etree import ElementTree as ET

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

        print(f'Libro agregado: id={id}, titulo={titulo}, autor={autor}, idioma={idioma}, categoria={categoria}, editorial={editorial}, copias={copias}')
    
    return jsonify({"message": "Archivo XML cargado correctamente"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)