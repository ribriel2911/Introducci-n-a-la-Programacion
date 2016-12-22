from collections import namedtuple
import random

TAMANNO_LETRA = 20
FPS_inicial = 2     #Velocidad inicial pero se puede alterar en el programa tambien (Ricky)
TIEMPO_MAX = 61     #Tiempo de juego (Ricky)
RELACION=0.75

PUNTOS="Score: "    #Ahora se modifica desde aca pustos y tiempo
TIEMPO="Time: "

IMAGEN_IZQUIERDA="chica"
NUMERO=random.randrange(1,6)

ANCHO = 800
ALTO = 600
COLOR_CANDIDATA = (255,255,255)
COLOR_LETRAS = []   #Cambie a lista (Ricky)
COLOR_FONDO = (0,0,0)
COLOR_PUNTOS = (255,215,0)
COLOR_TIEMPO = (0,255,255)
COLOR_TIEMPO_FINAL = (255,0,0)
Punto = namedtuple('Punto','x y')




