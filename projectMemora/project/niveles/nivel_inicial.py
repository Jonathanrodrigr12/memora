from project.utilidad.memora.memora import Memorama
from project.niveles.nivel_intermedio import NivelIntermedio

'''
Clase class se inicializa el primer nivel del juego con la cantidad de cartas y tamaño
'''
class NivelInical(Memorama):

    '''
    Constructor donde se incializa las clases y propiedades para la creación del primer nivel
    '''
    def __init__(self, ruta_fondo: str, ruta_imagenes: str, ruta_iamgenes_letras: str):
        super().__init__(ruta_fondo, ruta_imagenes, ruta_iamgenes_letras, "420x420",
        2, 2)

    '''
    Función que inicializa el primer nivel del juego
    '''    
    def iniciar_nivel(self):
        nivel_intermedio = NivelIntermedio
        self.iniciar_juego(nivel_intermedio)