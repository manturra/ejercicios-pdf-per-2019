class Libro():
    def __init__(self, nombre, tipo_prestamo, tipo_devolucion):
        self.nombre = nombre
        self.tipo_prestamo = tipo_prestamo
        self.tipo_devolucion = tipo_devolucion
    def prestamo(self):
        if self.tipo_prestamo == "largo":
            tiempo_prestado = "30 días"
        elif self.tipo_prestamo == "medio":
            tiempo_prestado = "15 días"
        else:
            tiempo_prestado = "7 días"
        return tiempo_prestado
    def devolucion(self):
        if tipo_devolucion == "regalo":
            tiempo_devolucion = "2 meses"
        else:
            tiempo_devolucion = "1 mes"
        return tiempo_devolucion
    def dame_info(self):
        return self.nombre,self.tipo_prestamo, self.tipo_devolucion

libro1 = Libro("Veinte mil leguas de viaje submarino", "largo", "regalo")
print(libro1.dame_info(), libro1.prestamo(), libro1.devolucion())
