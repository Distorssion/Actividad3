import tkinter as tki
from Piramide import Piramide
from tkinter import messagebox

class VentanaPiramide(tki.Toplevel):

    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Calculos Piramide")
        self.setLocationRelativeTo(280, 370)
        self.resizable(False, False)

    def setLocationRelativeTo(self, ancho: int, alto:int):
        x= (self.winfo_screenwidth() - ancho) / 2
        y= (self.winfo_screenheight() - alto) / 2
        self.geometry(str(ancho) + "x" + str(alto) + "+" + str(int(x)) +"+" + str(int(y)))



    def inicio(self):
        self.base = tki.Label(self, text="Base (cms):", anchor="w")
        self.base.place(x=20, y=20, width=100, height=23)
        self.campoBase = tki.Entry(self)
        self.campoBase.place(x=120, y=20, width=135, height=23)

        self.altura = tki.Label(self, text="Altura (cms):", anchor="w")
        self.altura.place(x=20, y=50, width=100, height=23)
        self.campoAltura = tki.Entry(self)
        self.campoAltura.place(x=120, y=50, width=135, height=23)

        self.apotema = tki.Label(self, text="Apotema (cms):", anchor="w")
        self.apotema.place(x=20, y=80, width=100, height=23)
        self.campoApotema = tki.Entry(self)
        self.campoApotema.place(x=120, y=80, width=135, height=23)

        self.calcular = tki.Button(
            self, text="Calcular",
            command=lambda: self.actionPerformed(self.calcular))
        self.calcular.place(x=120, y=110, width=135, height=23)

        self.volumen = tki.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=140, width=240, height=23)

        self.superficie = tki.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=170, width=240, height=23)

        #img

        self.imgPiramide = tki.PhotoImage(file="Act3/8.3/piramide.png")
        self.imgPiramide = self.imgPiramide.subsample(6,6)
        self.labelPiramide = tki.Label(self,image=self.imgPiramide)
        self.labelPiramide.place(x=57, y=187)

    def actionPerformed(self, evento):
        error = False
        try:
            base = float(self.campoBase.get())
            altura = float(self.campoAltura.get())
            apotema = float(self.campoApotema.get())
            piramide = Piramide(base, altura, apotema)
            self.volumen.config(
                text="Volumen: " + f"{piramide.calcularVolumen():.2f}"+" cm3")
            self.superficie.config(
                text="Superficie: " + f"{piramide.calcularSuperf():.2f}"+" cm2") 
        except Exception as e:
            print("Error real:", repr(e))
            error = True
        finally:
            if error:
                messagebox.showerror(
                    "Error", "Campo nulo o error en formato de número",
                    parent=self)