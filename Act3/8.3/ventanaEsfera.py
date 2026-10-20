import tkinter as tki
from Esfera import Esfera
from tkinter import messagebox


class VentanaEsfera(tki.Toplevel):
    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Calculos de la Esfera")
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

        self.calcular = tki.Button(
            self, text="Calcular",
            command=lambda: self.actionPerformed(self.calcular))
        self.calcular.place(x=110, y=50, width=130, height=23)

        self.volumen = tki.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=90, width=240, height=23)

        self.superficie = tki.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=120, width=240, height=23)

        self.imgEsfera = tki.PhotoImage(file="Act3/8.3/sphere.png")
        self.imgEsfera = self.imgEsfera.subsample(2,2)
        self.labelEsfera = tki.Label(self,image=self.imgEsfera)
        self.labelEsfera.place(x=77, y=150)

    def actionPerformed(self, evento):
        if evento == self.calcular:
            error = False
            try:
                radio = float(self.campoRadio.get())
                esfera = Esfera(radio)
                self.volumen.config(
                    text="Volumen: " + f"{esfera.calcularVolumen():.2f}"+" cm3")
                self.superficie.config(
                    text="Superficie: " + f"{esfera.calcularSuperf():.2f}"+" cm2")
            except Exception as e:
                print("Error real:", repr(e))
                error = True
            finally:
                if error:
                    messagebox.showerror(
                        "Error", "Campo nulo o error en formato de número",
                        parent=self)
                        