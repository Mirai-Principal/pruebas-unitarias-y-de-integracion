class Producto:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
   
    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad

class Inventario:
    def __init__(self):
        self.productos = {}
    
    def registrar_producto(self, producto):
        if producto.codigo == self.productos:
            raise ValueError("El producto ya existe")
        self.productos[producto.codigo] = producto

    def actualizar_inventario(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ValueError("Producto no existe")
        self.productos[codigo].actualizar_cantidad(cantidad)
    
    def consultar_producto(self, codigo):
        if codigo not in self.productos:
            raise ValueError("Producto no existe")
        producto = self.productos[codigo]
        return f"{producto.nombre} - Cantidad: {producto.cantidad}"
    
    def consultar_inventario(self):
        return [f"Producto: {producto.nombre} Codigo: {producto.codigo} Cantidad: {producto.cantidad}" for producto in self.productos.values()]