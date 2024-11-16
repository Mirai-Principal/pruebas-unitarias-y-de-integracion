# gestion_libros.py

class Libro:
    def __init__(self, id, titulo, autor, año, copias):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.copias = copias


class GestionLibros:
    def __init__(self):
        self.inventario = {}

    def registrar_libro(self, id, titulo, autor, año, copias):
        if id in self.inventario:
            return "El libro ya existe en el inventario."
        libro = Libro(id, titulo, autor, año, copias)
        self.inventario[id] = libro
        return "Libro registrado con éxito."

    def buscar_libro(self, criterio):
        resultados = [libro for libro in self.inventario.values() if criterio in (libro.titulo, libro.autor)]
        return resultados if resultados else "Libro no encontrado."

    def actualizar_inventario(self, id, cantidad):
        if id not in self.inventario:
            return "El libro no existe en el inventario."
        self.inventario[id].copias += cantidad
        return "Inventario actualizado."

    def eliminar_libro(self, id):
        if id not in self.inventario:
            return "El libro no existe en el inventario."
        del self.inventario[id]
        return "Libro eliminado del inventario."

