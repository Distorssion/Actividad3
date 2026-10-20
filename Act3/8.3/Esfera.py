import numpy as np
from figuraGeometrica import FiguraGeometrica

class Esfera(FiguraGeometrica):
    def __init__(self, radio:float):
        super().__init__()
        self.__radio = radio
        self.setVolumen(self.calcularVolumen())
        self.setSuperf(self.calcularSuperf())
    def calcularVolumen(self) -> float:
        return(4/3) * np.pi * np.pow(self.__radio, 3)
    def calcularSuperf(self)-> float:
        return 4* np.pi * np.pow(self.__radio,2)
    