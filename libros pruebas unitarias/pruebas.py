import unittest
from libros import GestionLibros

class TestGestionLibros(unittest.TestCase):
    def setUp(self):
        self.gestion = GestionLibros()
        self.gestion.registrar_libro(1, "Hiro Mashima", "Fairy Tail", 1943, 5)

    def test_registrar_libro_exitoso(self):
        resultado = self.gestion.registrar_libro(2, "Seirei", "Yuri Kitayama", 1967, 3)
        self.assertEqual(resultado, "Libro registrado con éxito.")

    def test_buscar_libro_no_existente(self):
        resultado = self.gestion.buscar_libro("Mi libro")
        self.assertEqual(resultado, "Libro no encontrado.")

    def test_actualizar_inventario_exitoso(self):
        resultado = self.gestion.actualizar_inventario(1, 3)
        self.assertEqual(resultado, "Inventario actualizado.")
        self.assertEqual(self.gestion.inventario[1].copias, 8)

    def test_eliminar_libro_inexistente(self):
        resultado = self.gestion.eliminar_libro(3)
        self.assertEqual(resultado, "El libro no existe en el inventario.")

if __name__ == '__main__':
    unittest.main()
