from tkinter import *
from project.utilidad.cartas.carta import Carta
from project.utilidad.ventana.ventana import Ventana
from tkinter import messagebox
import random


class Memorama(Ventana):

    def __init__(self, ruta_fondo: str, ruta_imagenes: str, ruta_iamgenes_letras: str, tamaño: str,
    tamaño_carta: int, cantidad_cartas: int):
        super().__init__(tamaño)
        self.botones = []
        self.cartas = []
        self.ruta_fondo = ruta_fondo
        self.temporal = Carta(ruta_fondo)
        self.valor_temporal = 0
        self.par = 0
        self.listo = True
        self.fondo = PhotoImage(file=ruta_fondo)
        self.ruta_imagenes = ruta_imagenes
        self.ruta_imagenes_letras = ruta_iamgenes_letras
        self.tamaño_carta = tamaño_carta
        self.cantidad_cartas = cantidad_cartas

    def iniciar_juego(self, ventana, nueva_ventana=True):
        self.crearTablero(nueva_ventana, ventana)
        self.revolver()
        self.crear_venta()
    
    def crearTablero(self, nueva_venta, venta):
        i = 0
        contador = 0
        while i<self.tamaño_carta:
            j = 0
            while j<self.tamaño_carta:
                btn = Button(self.ventana, command=lambda a = contador: self.revisar(a, nueva_venta, venta),
                height=70, width=70, image=self.fondo)
                btn.place(x=(j+1)*70, y=(i+1)*70)
                self.botones.append(btn)
                j+=1
                contador+=1
            i+=1    


    def revolver(self):
        i = 1
        while(i<=self.cantidad_cartas):
            carta1 = Carta(self.ruta_fondo)
            carta1.valor = i
            carta1.foto = PhotoImage(file=self.ruta_imagenes+str(i)+".gif")
            carta2 = Carta(self.ruta_fondo)
            carta2.valor = i
            carta2.foto = PhotoImage(file=self.ruta_imagenes_letras+str(i)+".gif")
            self.cartas.append(carta1)
            self.cartas.append(carta2)
            i+=1
        cartasTemporal = []    
        while len(self.cartas)>0:
            posicion = random.randrange(0, len(self.cartas))
            cartasTemporal.append(self.cartas.pop(posicion))
        self.cartas = cartasTemporal
    
    def revisar(self,a, nueva_venta, venta):
        if self.listo == True and self.cartas[a].oculto==True:
            self.botones[a].config(image=self.cartas[a].foto)
            if self.par==0:
                self.temporal = self.cartas[a]
                self.cartas[a].oculto = False
                self.temporal.posicion = a
                self.par = 1
            elif self.par==1:
                self.par = 0    
                if self.temporal.valor == self.cartas[a].valor:
                    self.cartas[a].oculto = False
                    bandera = True
                    for elemento in self.cartas:
                        if elemento.oculto == True:
                            bandera = False
                            break
                    self.finalizar_juego(bandera, nueva_venta, venta)
                    
                else: 
                    self.valor_temporal = a
                    self.listo = False
                    self.ventana.after(500, self.tapar)
    
    def tapar(self):
        self.cartas[self.temporal.posicion].oculto = True
        self.botones[self.temporal.posicion].config(image=self.fondo)
        self.botones[self.valor_temporal].config(image=self.fondo)
        self.listo = True

    
    def finalizar_juego(self, bandera, nueva_venta, venta):
        if bandera == True:
            self.ventana.destroy()
            if nueva_venta:
                venta(self.ruta_fondo, self.ruta_imagenes, self.ruta_imagenes_letras).iniciar_nivel()
            else:
                messagebox.showinfo("Ganaste", "Felcidades, gnaaste")