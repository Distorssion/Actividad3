import numpy as np

from figuraGeometrica import FiguraGeometrica

class Piramide(FiguraGeometrica):

    def __init__(self, base: float, altura: float, apotema: float):
        super().__init__()
        self.__base = base
        self.__altura = altura
        self.__apotema = apotema
        self.setVolumen(self.calcularVolumen())
        self.setSuperf(self.calcularSuperf())

    def calcularVolumen(self)-> float:
        return(np.pow(self.__base,2) * self.__altura) / 3
    
    def calcularSuperf(self)->float:
        areaB = np.pow(self.__base,2)

        areaL = 2 * self.__base * self.__apotema
        return areaB + areaL
    