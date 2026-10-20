#Prisma rectangular

from figuraGeometrica import FiguraGeometrica
#import numpy as np
class Prisma(FiguraGeometrica):
    def __init__(self, largoB:float, anchoB:float, altura: float):
        super().__init__()
        self.__largoB = largoB
        self.__anchoB= anchoB
        self.__altura = altura
        self.setVolumen(self.calcularVolumen())
        self.setSuperf(self.calcularSuperf())

    def calcularVolumen(self) -> float:
        return self.__largoB * self.__anchoB* self.__altura
    def calcularSuperf(self) -> float:
        areaBase = self.__largoB * self.__anchoB
        areaFrente = self.__largoB * self.__altura
        areaLateral = self.__anchoB * self.__altura
        return 2.0 * (areaBase + areaFrente + areaLateral)