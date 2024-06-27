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
            usuario = {
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