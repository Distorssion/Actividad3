# Ejercicio 8.2 
import tkinter as tkt
from tkinter import messagebox
from Notas import Notas
from tkinter import font



class VentanaPrincipal(tkt.Tk):

    def __init__(self):
        super().__init__()
        self.inicio()
        self.title("Notas del estudiante")             
        self.setLocationRelativeTo(250, 350)   
        self.resizable(False, False)            

    def setLocationRelativeTo(self, ancho, alto):
        x = (self.winfo_screenwidth() - ancho) / 2
        y = (self.winfo_screenheight() - alto) / 2
        self.geometry(str(ancho) + "x" + str(alto) + "+" + str(int(x)) +"+" + str(int(y)))

    def inicio(self):
        #estilo
        self.negrita = font.Font(family="Helvetica", size=10, weight="bold")
        self.cursiva = font.Font(family="Helvetica", size=10, slant="italic", weight = "bold")

        self.nota1 = tkt.Label(self, text="Nota #1:  ", anchor="center", font=self.negrita)
        self.nota1.place(x=47, y=20, width=80,height=23)
        self.Note1Space = tkt.Entry(self)
        self.Note1Space.place(x=117, y=20, width=80,height=23)
        self.nota2 = tkt.Label(self, text="Nota #2:  ", anchor="center", font=self.negrita)
        self.nota2.place(x=47, y=50, width=80, height=23)
        self.Note2Space = tkt.Entry(self)
        self.Note2Space.place(x=117, y=50, width=80, height=23)
        self.nota3 = tkt.Label(self, text="Nota #3:  ", anchor="center", font=self.negrita)
        self.nota3.place(x=47, y=80, width=80, height=23)
        self.Note3Space = tkt.Entry(self)
        self.Note3Space.place(x=117, y=80, width=80, height=23)
        self.nota4 = tkt.Label(self, text="Nota #4:  ", anchor="center", font=self.negrita)
        self.nota4.place(x=47, y=110, width=80, height=23)
        self.Note4Space = tkt.Entry(self)
        self.Note4Space.place(x=117, y=110, width=80, height=23)
        self.nota5 = tkt.Label(self, text="Nota #5:  ", anchor="center", font=self.negrita)
        self.nota5.place(x=47, y=140, width=80, height=23)
        self.Note5Space = tkt.Entry(self)
        self.Note5Space.place(x=117, y=140, width=80, height=23)

        #botones
        self.calcular = tkt.Button(
            self, text="Calcular", command=lambda: self.actionPerformed(self.calcular), font=self.cursiva)
        self.calcular.place(x=47, y=180, width=77, height=23)

        self.limpiar = tkt.Button(
            self, text="Limpiar", command=lambda: self.actionPerformed(self.limpiar), font=self.cursiva)
        self.limpiar.place(x=130, y=180, width=77, height=23)

        
        self.promedio = tkt.Label(self, text="Promedio = ", anchor="w", font=self.negrita)
        self.promedio.place(x=47, y=210, width=200, height=23)

        self.desviacion = tkt.Label(self, text="Desviación = ", anchor="w", font=self.negrita)
        self.desviacion.place(x=47, y=240, width=200, height=23)

        self.mayor = tkt.Label(self, text="Nota mayor = ", anchor="w", font=self.negrita)
        self.mayor.place(x=47, y=270, width=200, height=23)

        self.menor = tkt.Label(self, text="Nota menor = ", anchor="w", font=self.negrita)
        self.menor.place(x=47, y=300, width=200, height=23)

    def actionPerformed(self, evento):
            if evento == self.calcular:
                notas = Notas()
                spaceNota = [self.Note1Space, self.Note2Space, self.Note3Space, self.Note4Space, self.Note5Space]

                #validar que estén las 5 notas y que el valor ingresado sea numerico
                
                for i in range(5):
                    if spaceNota[i].get().strip() == "":
                        messagebox.showwarning("Valor faltante",f"No se ingresaron las 5 notas, falta la nota # {i+1}")
                        return
                try:
                    for i in range(5):
                        notas.listaNotas[i] = float(spaceNota[i].get())
                except ValueError:
                    messagebox.showerror("Valor invalido","Ingrese un valor numérico.")
                    return

                    
                self.promedio.config( text="Promedio = " + f"{notas.calcularPromedio():.2f}")
                self.desviacion.config( text="Desviación estándar = " + f"{notas.calcularDesv():.2f}")
                self.mayor.config(text="Nota más alta = " + str(notas.calcularMayor()))
                self.menor.config(text="Nota más baja = " + str(notas.calcularMenor()))

            if evento == self.limpiar:
                self.Note1Space.delete(0,tkt.END)
                self.Note2Space.delete(0,tkt.END)
                self.Note3Space.delete(0,tkt.END)
                self.Note4Space.delete(0,tkt.END)
                self.Note5Space.delete(0,tkt.END)