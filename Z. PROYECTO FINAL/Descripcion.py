#Pregunta:
#¿Cómo promover e incentivar el conocimiento sobre seguridad de la
#información en adolescentes?
#Descripción:
#En el mundo moderno el acceso a internet se ha convertido en un elemento
#fundamental. Jóvenes y niños están interactuando con dispositivos móviles y
#servicios de internet mucho más rápido que en años anteriores.
#Una de las preocupaciones más grandes de los padres es el poder proteger la
#información e integridad de sus hijos, y evitar que sean víctimas de los
#diversos delitos que pueden cometerse en la red.
#Se busca encontrar una forma didáctica, directa y eficaz para enseñar a los
#adolescentes y a sus padres el uso correcto y responsable de dispositivos
#electrónicos y las bases principales de seguridad de la información

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import os
import webbrowser
import random

class Aplicacion:
    def __init__(self):
        self.raiz=Tk()
        self.raiz.title("Descripción")
        self.raiz.geometry("500x500")
        self.raiz.resizable(width=False, height=False)
        self.raiz.config(bg="white")
        self.raiz.iconbitmap("icono.ico")
        self.raiz.mainloop()

    def cerrar(self):
        self.raiz.destroy()

    def abrir(self):
        self.raiz.deiconify()

    def minimizar(self):
        self.raiz.iconify()

    def ayuda(self):
        messagebox.showinfo("Ayuda", "Para acceder a la ayuda, por favor, presione el botón de la esquina superior derecha")

    def acerca(self):
        messagebox.showinfo("Acerca de", "Proyecto Final para la materia de EdD-AdA\nHecho por:\nLaura Camila Diaz Delgado\n\nProfesor:\nNury Farelo")

    def menu(self):
        self.barraMenu=Menu(self.raiz)
        self.raiz.config(menu=self.barraMenu)
        self.archivoMenu=Menu(self.barraMenu, tearoff=0)
        self.archivoMenu.add_command(label="Salir", command=self.cerrar)
        self.barraMenu.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.ayudaMenu=Menu(self.barraMenu, tearoff=0)
        self.ayudaMenu.add_command(label="Ayuda", command=self.ayuda)
        self.ayudaMenu.add_command(label="Acerca de", command=self.acerca)
        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)

    def botones(self):
        self.boton1=Button(self.raiz, text="Siguiente", command=self.siguiente)
        self.boton1.place(x=400, y=450)
        self.boton2=Button(self.raiz, text="Anterior", command=self.anterior)
        self.boton2.place(x=300, y=450)
        self.boton3=Button(self.raiz, text="Menú", command=self.regresar)
        self.boton3.place
    
    def siguiente(self):
        self.raiz.withdraw()
        self.raiz2=Toplevel()
        self.raiz2.title("Descripción")
        self.raiz2.geometry("500x500")
        self.raiz2.resizable(width=False, height=False)
        self.raiz2.config(bg="white")
        self.raiz2.iconbitmap("icono.ico")
        self.raiz2.protocol("WM_DELETE_WINDOW", self.cerrar2)
        self.raiz2.mainloop()
    
    def anterior(self):
        self.raiz.withdraw()
        self.raiz3=Toplevel()
        self.raiz3.title("Descripción")
        self.raiz3.geometry("500x500")
        self.raiz3.resizable(width=False, height=False)
        self.raiz3.config(bg="white")
        self.raiz3.iconbitmap("icono.ico")
        self.raiz3.protocol("WM_DELETE_WINDOW", self.cerrar3)
        self.raiz3.mainloop()
    
    #ejecuta el programa
    def regresar(self):
        self.raiz.withdraw()
        self.raiz4=Toplevel()
        self.raiz4.title("Menú")
        self.raiz4.geometry("500x500")
        self.raiz4.resizable(width=False, height=False)
        self.raiz4.config(bg="white")
        self.raiz4.iconbitmap("icono.ico")
        self.raiz4.protocol("WM_DELETE_WINDOW", self.cerrar4)
        self.raiz4.mainloop()
    
    def cerrar2(self):
        self.raiz2.destroy()
        self.abrir()
    
    def cerrar3(self):
        self.raiz3.destroy()
        self.abrir()
    
    def cerrar4(self):
        self.raiz4.destroy()
        self.abrir()
    
    def iniciar(self):
        self.menu()
        self.botones()
    
        
