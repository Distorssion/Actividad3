import tkinter as tki
from Cilindro import Cilindro
from tkinter import messagebox
#import os


class VentanaCilindro(tki.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Calculos del Cilindro")
        self.setLocationRelativeTo(280, 300)
        self.resizable(False, False)

    def setLocationRelativeTo(self, ancho: int, alto:int):
        x= (self.winfo_screenwidth() - ancho) / 2
        y= (self.winfo_screenheight() - alto) / 2
        self.geometry(str(ancho) + "x" + str(alto) + "+" + str(int(x)) +"+" + str(int(y)))


    def inicio(self):
        self.radio = tki.Label(self, text="Radio (cms):", anchor="w")
        self.radio.place(x=20, y=20, width=90, height=23)
        self.campoRadio = tki.Entry(self)
        self.campoRadio.place(x=110, y=20, width=130, height=23)

        self.altura = tki.Label(self, text="Altura (cms):", anchor="w")
        self.altura.place(x=20, y=50, width=90, height=23)
        self.campoAltura = tki.Entry(self)
        self.campoAltura.place(x=110, y=50, width=130, height=23)

        self.calcular = tki.Button(
            self, text="Calcular",
            command=lambda: self.actionPerformed(self.calcular))
        self.calcular.place(x=110, y=80, width=130, height=23)

        self.volumen = tki.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=110, width=240, height=23)

        self.superficie = tki.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=140, width=240, height=23)

        #img de la fig
        self.imgCilindro = tki.PhotoImage(file="Act3/8.3/cilinder.png")
        self.imgCilindro = self.imgCilindro.subsample(8,8)
        self.labelCilindro = tki.Label(self,image=self.imgCilindro)
        self.labelCilindro.place(x=77, y=160)
        
    def actionPerformed(self, evento):
        error = False
        try:
            radio = float(self.campoRadio.get())
            altura = float(self.campoAltura.get())
            cilindro = Cilindro(radio, altura)
            self.volumen.config(
                text="Volumen: " + f"{cilindro.calcularVolumen():.2f}"+ " cm3")
            self.superficie.config(
                text="Superficie: " + f"{cilindro.calcularSuperf():.2f}"+ " cm2")
        except Exception as e:
            print("Error real:", repr(e))
            error = True
        finally:
            if error:
                messagebox.showerror(
                    "Error", "Campo nulo o error en formato de número",
                    parent=self)