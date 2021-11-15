from project.utilidad.memora.memora import Memorama
from project.utilidad.memora.memora import Memorama

class NivelIntermedio(Memorama):
    def __init__(self, ruta_fondo: str, ruta_imagenes: str, ruta_iamgenes_letras: str):
        super().__init__(ruta_fondo, ruta_imagenes, ruta_iamgenes_letras, "425x425",
        4, 8)

    def iniciar_nivel(self):
        self.iniciar_juego(ventana=None, nueva_ventana=False)

        