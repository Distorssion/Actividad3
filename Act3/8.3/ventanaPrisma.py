
import tkinter as tki
from tkinter import messagebox
from Prisma import Prisma


class VentanaPrisma(tki.Toplevel):

    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Prisma")
        self.setLocationRelativeTo(280, 370)
        self.resizable(False, False)

    def setLocationRelativeTo(self, ancho: int, alto: int):
        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def inicio(self):
        self.largo = tki.Label(self, text="Largo (cms):", anchor="w")
        self.largo.place(x=20, y=20, width=100, height=23)
        self.campoLargo = tki.Entry(self)
        self.campoLargo.place(x=120, y=20, width=135, height=23)

        self.ancho = tki.Label(self, text="Ancho (cms):", anchor="w")
        self.ancho.place(x=20, y=50, width=100, height=23)
        self.campoAncho = tki.Entry(self)
        self.campoAncho.place(x=120, y=50, width=135, height=23)

        self.altura = tki.Label(self, text="Altura (cms):", anchor="w")
        self.altura.place(x=20, y=80, width=100, height=23)
        self.campoAltura = tki.Entry(self)
        self.campoAltura.place(x=120, y=80, width=135, height=23)

        self.calcular = tki.Button(
            self, text="Calcular",
            command=lambda: self.actionPerformed(self.calcular))
        self.calcular.place(x=120, y=110, width=135, height=23)

        self.volumen = tki.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=140, width=240, height=23)

        self.superficie = tki.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=170, width=240, height=23)

        self.imgPrisma = tki.PhotoImage(file="Act3/8.3/prisma.png")
        self.imgPrisma = self.imgPrisma.subsample(3,3)
        self.labelPrisma = tki.Label(self,image=self.imgPrisma)
        self.labelPrisma.place(x=77, y=187)

    def actionPerformed(self, evento):
        error = False
        try:
            largo = float(self.campoLargo.get())
            ancho = float(self.campoAncho.get())
            altura = float(self.campoAltura.get())
            prisma = Prisma(largo, ancho, altura)
            self.volumen.config(
                text="Volumen: " + f"{prisma.calcularVolumen():.2f}"+" cm3")
            self.superficie.config(
                text="Superficie: " + f"{prisma.calcularSuperf():.2f}"+" cm2")
        except Exception as e:
            error = True
        finally:
            if error:
                messagebox.showerror("Error", "Campo nulo o error en formato de número",parent=self)