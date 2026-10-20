from figuraGeometrica import FiguraGeometrica
import numpy as np
class Cubo(FiguraGeometrica):
    def __init__(self, longitudL: float):
        super().__init__()
        self.__longitudL = longitudL
        self.setVolumen(self.calcularVolumen())
        self.setSuperf(self.calcularSuperf())

    def calcularVolumen(self) -> float:
        return np.pow(self.__longitudL,3)
    def calcularSuperf(self) -> float:
        return 6 * np.pow(self.__longitudL,2)