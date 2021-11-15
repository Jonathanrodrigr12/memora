from project.utilidad.memora.memora import Memorama
from project.niveles.nivel2 import NivelIntermedio

class NivelInical(Memorama):
    def __init__(self, ruta_fondo: str, ruta_imagenes: str, ruta_iamgenes_letras: str):
        super().__init__(ruta_fondo, ruta_imagenes, ruta_iamgenes_letras, "420x420",
        2, 2)
        

    def iniciar_nivel(self):
        nivel_intermedio = NivelIntermedio
        self.iniciar_juego(nivel_intermedio)