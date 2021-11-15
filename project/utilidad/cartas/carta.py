from tkinter import *

class Carta:
    def __init__(self, path:str):
        self.valor = 0
        self.posicon = 0
        self.oculto = True
        self.foto = PhotoImage(file=path)