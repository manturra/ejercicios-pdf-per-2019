class Alumno():
    def __init__(self,matricula,nombre,nota1,nota2,nota3):
        self.matricula = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def calcula_notafinal(self):
        nota_final = (self.nota1+self.nota2+self.nota3)/3
        return nota_final
    def comprueba_nota(self):
        nota_final = (self.nota1+self.nota2+self.nota3)/3
        if nota_final >= 4.8:
            evaluacion = "aprobada"
        else:
            evaluacion = "suspensa"
        return evaluacion
    def dame_info(self):
        return self.matricula, self.nombre

alumno1 = Alumno("biología","sandra",9,9.5,8.5)
print(alumno1.dame_info(),alumno1.calcula_notafinal(),alumno1.comprueba_nota())
