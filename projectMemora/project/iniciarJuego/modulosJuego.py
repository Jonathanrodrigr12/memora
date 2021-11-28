from tkinter import *
from project.utilidad.ventana.ventana import Ventana
from project.niveles.nivel_inicial import NivelInical
from PIL import ImageTk, Image

'''
Clase ModulosJuego se inicializa la venta de los tipos de juegos
para el juego memora
'''
class ModulosJuego(Ventana):
    
    '''
    Constructor donde se incializa las clases y propiedades para la creación de los modulos de juego
    '''
    def __init__(self):
        super().__init__("625x500")
        self.pixelVirtual1 = ImageTk.PhotoImage(Image.open("./images/background/opciones/colores.gif"))
        self.pixelVirtual2 = ImageTk.PhotoImage(Image.open("./images/background/opciones/fondoAnimales.gif"))
        self.pixelVirtual3 = ImageTk.PhotoImage(Image.open("./images/background/opciones/numeros.gif"))
        self.pixelVirtual4 = ImageTk.PhotoImage(Image.open("./images/background/menuOpciones/fondoNiños.gif"))
        
        fm = Frame(self.ventana)
        background_label = Label(fm, image=self.pixelVirtual4) 
        background_label.place(x=0, y=0, relwidth=1, relheight=1) 
        Button(fm, text='Colores', image=self.pixelVirtual1, width=100,
                           height=100,command=self.iniciarColores).pack(side=LEFT, expand=YES)
        Button(fm, text='Animales',image=self.pixelVirtual2,width=100,
                           height=100,command=self.iniciarAnimales).pack(side=LEFT, expand=YES)
        Button(fm, text='Numeros',image=self.pixelVirtual3,width=100,
                           height=100,command=self.iniciarNumeros).pack(side=LEFT, expand=YES)
        fm.pack(fill=BOTH, expand=YES)

    '''
    Metodo encargado de inicializar la ventana del juego para colores
    '''
    def iniciarColores(self):
        self.ventana.destroy()
        obj = NivelInical("./images/background/ventana/colores.png",
          "./images/colors/colors/","./images/colors/letterColors/")
        obj.iniciar_nivel()
        
    '''
    Metodo encargado de inicializar la ventana del juego para numeros
    '''
    def iniciarNumeros(self):
        self.ventana.destroy()
        obj = NivelInical("./images/background/ventana/numeros.png",
            "./images/numbers/numbers/","./images/numbers/letterNumbers/")  
        obj.iniciar_nivel()

    '''
    Metodo encargado de inicializar la ventana del juego para animales
    '''
    def iniciarAnimales(self):
        self.ventana.destroy()
        obj = NivelInical("./images/background/ventana/animal.png",
        "./images/animals/animal/","./images/animals/letterAnimal/")
        obj.iniciar_nivel()