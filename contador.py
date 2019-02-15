class Contador():
    def __init__(self,numero=None):
        if numero:
            self.numero = numero
        else:
            self.numero = 0
    def incrementar_contador(self):
        numero_incrementado = self.numero+2
        return numero_incrementado
    def decrementar_contador(self):
        numero_decrementado = self.numero-3
        return numero_decrementado

numero1 = Contador()
print(numero1.incrementar_contador())
