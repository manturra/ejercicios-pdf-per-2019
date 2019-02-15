class Empleado():
    def __init__(self,nombre,salario,puesto,tasa):
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto
        self.tasa = tasa
    def Calcula_impuestos(self):
        impuesto = self.tasa*self.salario
        return impuesto
    def get_info(self):
        info = (self.salario,self.puesto,self.tasa)
        print("La información del empleado", self.nombre, info)

empleado1 = Empleado("Carlos",5000,"jefe de cocina",0.3)
empleado1.get_info()
print(empleado1.Calcula_impuestos())
