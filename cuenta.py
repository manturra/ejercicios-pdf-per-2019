class Cuenta():
    def __init__(self,dinero,ingreso,reintegro,transferencia):
        self.dinero=dinero
        self.ingreso=ingreso
        self.reintegro=reintegro
        self.transferencia=transferencia
    def get_ingreso(self):
        cuenta = self.dinero+self.ingreso
        return cuenta
    def get_reintegro(self):
        cuenta = self.dinero-self.reintegro
        return cuenta
    def get_transferencia(self):
        cuenta = self.dinero-self.transferencia
        cuenta2 = self.transferencia
        return cuenta, cuenta2

oscar_cuenta = Cuenta(60000, 2000, 1000, 5000)
print(oscar_cuenta.get_ingreso())
print(oscar_cuenta.get_reintegro())
print(oscar_cuenta.get_transferencia())
