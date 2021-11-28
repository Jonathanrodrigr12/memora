from project.utilidad.memora.memora import Memorama
from project.utilidad.memora.memora import Memorama
from project.niveles.nivel_dificil import NivelDificil

'''
Clase class se inicializa el segundo nivel del juego con la cantidad de cartas y tamaño
'''
class NivelIntermedio(Memorama):

    '''
    Constructor donde se incializa las clases y propiedades para la creación del segundo nivel
    '''
    def __init__(self, ruta_fondo: str, ruta_imagenes: str, ruta_iamgenes_letras: str):
        super().__init__(ruta_fondo, ruta_imagenes, ruta_iamgenes_letras, "425x425",
        4, 8)
    
    '''
    Función que inicializa el segundo nivel del juego
    '''  
    def iniciar_nivel(self):
        nivel_dificil = NivelDificil
        self.iniciar_juego(ventana=nivel_dificil)

        