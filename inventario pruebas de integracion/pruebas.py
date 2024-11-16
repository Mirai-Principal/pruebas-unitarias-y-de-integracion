import unittest
from inventario import Producto, Inventario

class TestProducto(unittest.TestCase):
    def test_crear_producto(self):
        producto = Producto(1, "manzana", 10)
        self.assertEqual(producto.codigo, 1)
        self.assertEqual(producto.nombre, "manzana")
        self.assertEqual(producto.cantidad, 10)
    def test_actualizar_cantidad(self):
        producto = Producto(1, "manzana", 10)
        producto.actualizar_cantidad(15)
        cantidad_esperada = 25
        self.assertEqual(producto.cantidad, 25)
        
        producto.actualizar_cantidad(-5)
        cantidad_esperada = 20
        self.assertEqual(producto.cantidad, 20)

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()
        self.producto1 = Producto(1, "naranja", 10)
        self.producto2 = Producto(2, 'fresa', 5)
    
    def test_registrar_producto(self):
        self.inventario.registrar_producto(self.producto1)
        resultado = self.inventario.consultar_producto(self.producto1.codigo)
        self.assertEqual(resultado, "naranja - Cantidad: 10")

    def test_actualizar_inventario(self):
        self.inventario.registrar_producto(self.producto1)
        self.inventario.actualizar_inventario(1, 8)
        resultado = self.inventario.consultar_producto(self.producto1.codigo)
        self.assertEqual(resultado, "naranja - Cantidad: 18")

class TestIntegracion(unittest.TestCase):
    def test_agregar_y_actualizar_varios_productos(self):
        #definiendo productos
        self.inventario = Inventario()
        self.producto1 = Producto(1, "naranja", 10)
        self.producto2 = Producto(2, 'fresa', 5)

        #add to inventario
        self.inventario.registrar_producto(self.producto1)
        self.inventario.registrar_producto(self.producto2)

        ##update inventario
        self.inventario.actualizar_inventario(1, 5)
        self.inventario.actualizar_inventario(2, -2)

        #consutar inventario
        resultado = self.inventario.consultar_inventario()
        self.assertIn("Producto: naranja Codigo: 1 Cantidad: 15", resultado)
        self.assertIn("Producto: fresa Codigo: 2 Cantidad: 3", resultado)
 
if __name__ == "__main__":
    unittest.main()