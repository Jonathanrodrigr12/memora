from tkinter import *

class Ventana:
    def __init__(self, tamaño: str):
        self.ventana = Tk()
        self.ventana.title("Memorama")
        self.ventana.geometry(tamaño)
        

    def crear_venta(self):
        self.ventana.mainloop()