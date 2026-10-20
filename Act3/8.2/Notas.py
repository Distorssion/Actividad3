
import numpy as np

class Notas:
    def __init__(self):
        self.listaNotas= [0.0,0.0,0.0,0.0,0.0]
        self.largo = len(self.listaNotas)
    def calcularPromedio(self)->float:
        suma = 0
        for i in range(self.largo):
            suma = suma+self.listaNotas[i]

        return suma/self.largo
    def calcularDesv(self)->float:
        promedio = self.calcularPromedio()
        suma=0
        for i in range(self.largo):
            suma+=np.pow(self.listaNotas[i]-promedio,2)
        return np.sqrt(suma/self.largo)
    def calcularMenor(self)->float:
        menorN = self.listaNotas[0]
        for i in range(self.largo):
            if self.listaNotas[i]<menorN:
                menorN = self.listaNotas[i]
        return menorN
    def calcularMayor(self)->float:
        mayorN = self.listaNotas[0]
        for i in range(self.largo):
            if self.listaNotas[i]>mayorN:
                mayorN = self.listaNotas[i]
        return mayorN
    
notas = Notas()
print(notas.calcularPromedio())