from tkinter import *

'''
Clase ventana donde se crea la ventana de ejecución para si posteriormente
agregarle las cartas para que comience el juego
'''
class Ventana:
    '''
    Constructor donde se incializa las clases y propiedades para la creación del juego
    '''
    def __init__(self, tamaño: str):
        self.ventana = Tk()
        self.ventana.title("Memorama")
        self.ventana.geometry(tamaño) 
        self.ventana.configure(background='sky blue')
    
    '''
    Metodo que lanza la ejecución de la venta y nos deja interactuar con ella.
    '''
    def crear_venta(self):
        self.ventana.mainloop()