class FiguraGeometrica:
    def __init__(self):
        self.__volumen = 0
        self.__superficie = 0
    # setter y getters de lasfiguras
    def setVolumen(self, volumen: float):
        self.__volumen = volumen
    def setSuperf(self, superficie: float):
        self.__superficie = superficie
    def getVolumen(self)-> float:
        return self.__volumen
    def getSuperf(self) -> float:
        return self.__superficie