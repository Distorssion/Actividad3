import tkinter as tki
from tkinter import font
from ventanaCilindro import VentanaCilindro
from ventanaPiramide import VentanaPiramide
from ventanaEsfera import VentanaEsfera
from ventanaCubo import VentanaCubo
from ventanaPrisma import VentanaPrisma




class VentanaPrincipal(tki.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Figuras")
        self.setLocationRelativeTo(200, 300)
        self.resizable(False, False)

    def setLocationRelativeTo(self, ancho: int, alto:int):
        x= (self.winfo_screenwidth() - ancho) / 2
        y= (self.winfo_screenheight() - alto) / 2
        self.geometry(str(ancho) + "x" + str(alto) + "+" + str(int(x)) +"+" + str(int(y)))
    
    
    def inicio(self):
        self.negrita = font.Font(family="Helvetica", size=8, weight="bold")
        self.cursiva = font.Font(family="Helvetica", size=10, slant="italic", weight = "bold")
        tituloFig = tki.Label(self,text = " Lista de Figuras Geometricas ", anchor = "center", font = self.cursiva,
                               borderwidth = "1", relief = "solid")
        tituloFig.place(x=5,y=17)
        self.cilindro = tki.Button(
            self, text="Cilindro", font=self.negrita,
            command=lambda: self.actionPerformed(self.cilindro))
        self.cilindro.place(x=52, y=60, width=100, height=23)

        self.esfera = tki.Button(
            self, text="Esfera", font=self.negrita,
            command=lambda: self.actionPerformed(self.esfera))
        self.esfera.place(x=52, y=110, width=100, height=23)

        self.piramide = tki.Button(
            self, text="Piramide", font=self.negrita,
            command=lambda: self.actionPerformed(self.piramide))
        self.piramide.place(x=52, y=160, width=100, height=23)

        self.cubo = tki.Button(
            self, text = "Cubo", font = self.negrita,
            command = lambda: self.actionPerformed(self.cubo))
        self.cubo.place(x=52, y=210, width=100, height = 23)

        self.prisma = tki.Button(
            self, text = "Prisma", font=self.negrita,
            command = lambda: self.actionPerformed(self.prisma))
        self.prisma.place(x=52, y = 260, width=100, height=23)
        



    def actionPerformed(self, evento):
        if evento == self.esfera:
            VentanaEsfera()
        if evento == self.cilindro:
            VentanaCilindro()
        if evento == self.piramide:
            VentanaPiramide()
        if evento == self.cubo:
            VentanaCubo()
        if evento == self.prisma:
            VentanaPrisma()



    