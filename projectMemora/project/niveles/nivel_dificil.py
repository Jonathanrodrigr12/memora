from project.utilidad.memora.memora import Memorama
from project.utilidad.memora.memora import Memorama

'''
Clase class se inicializa el segundo tercer del juego con la cantidad de cartas y tamaño
'''
class NivelDificil(Memorama):

    '''
    Constructor donde se incializa las clases y propiedades para la creación del tercer nivel
    '''
    def __init__(self, ruta_fondo: str, ruta_imagenes: str, ruta_iamgenes_letras: str):
        super().__init__(ruta_fondo, ruta_imagenes, ruta_iamgenes_letras, "545x545",
        6, 18)

    '''
    Función que inicializa el tercer nivel del juego
    '''  
    def iniciar_nivel(self):
        self.iniciar_juego(ventana=None, nueva_ventana=False)

        