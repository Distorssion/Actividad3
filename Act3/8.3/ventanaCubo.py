import tkinter as tki
from Cubo import Cubo
from tkinter import messagebox


class VentanaCubo(tki.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Calculos del Cubo")
        self.setLocationRelativeTo(280, 315)
        self.resizable(False, False)

    def setLocationRelativeTo(self, ancho: int, alto:int):
        x= (self.winfo_screenwidth() - ancho) / 2
        y= (self.winfo_screenheight() - alto) / 2
        self.geometry(str(ancho) + "x" + str(alto) + "+" + str(int(x)) +"+" + str(int(y)))

    def inicio(self):
        self.longLado = tki.Label(self, text="Lado (cm):", anchor="w")
        self.longLado.place(x=20, y=20, width=90, height=23)
        self.campolongLado = tki.Entry(self)
        self.campolongLado.place(x=110, y=20, width=130, height=23)

        self.calcular = tki.Button(
            self, text="Calcular",
            command=lambda: self.actionPerformed(self.calcular))
        self.calcular.place(x=110, y=50, width=130, height=23)

        self.volumen = tki.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=90, width=240, height=23)

        self.superficie = tki.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=120, width=240, height=23)


        #img
        self.imgCubo = tki.PhotoImage(file = "Act3/8.3/cubo.png")
        self.imgCubo = self.imgCubo.subsample(3,3)
        self.labelCubo = tki.Label(self, image = self.imgCubo)
        self.labelCubo.place(x=55, y=140)
        


    def actionPerformed(self, evento):
        if evento == self.calcular:
            error = False
            try:
                longLado = float(self.campolongLado.get())
                cubo = Cubo(longLado)
                self.volumen.config(
                    text="Volumen: " + f"{cubo.calcularVolumen():.2f}"+" cm3")
                self.superficie.config(
                    text="Superficie: " + f"{cubo.calcularSuperf():.2f}"+" cm2")
            except Exception as e:
                print("Error real:", repr(e))
                error = True
            finally:
                if error:
                    messagebox.showerror(
                        "Error", "Campo nulo o error en formato de número",
                        parent=self)