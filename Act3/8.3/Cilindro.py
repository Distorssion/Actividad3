from figuraGeometrica import FiguraGeometrica
import numpy as np
class Cilindro(FiguraGeometrica):
    def __init__(self, radio:float, altura:float):
        super().__init__()
        self.__altura = altura
        self.__radio = radio
        self.setVolumen(self.calcularVolumen())
        self.setSuperf(self.calcularSuperf())

    def calcularVolumen(self) -> float:
        return np.pi * self.__altura * np.pow(self.__radio, 2)
    def calcularSuperf(self) -> float:
        areaLado1 = 2 * np.pi * self.__radio * self.__altura
        areaLado2 = 2* np.pi * np.pow(self.__radio, 2)
        return areaLado1 + areaLado2
    