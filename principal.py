#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, random, sys, math

import pygame

from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *
import pickle





#Programa Pirncipal ejecuta Main

class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (255, 255, 255))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 500
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('cursor23elbueno.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa un menÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº con opciones para un juego"

    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('fuente2.ttf', 40)
        x = 500
        y = 300
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = True

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la funciÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³n asociada a la opciÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³n.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor estÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opciÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³n del menÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

#Funcion principal
def funcionJuego():

        diferencia= pygame.time.get_ticks()/1000
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Fast fast...") #Cambia el nombre del juego (Ricky)
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #Seleccione fondo (Ricky)
        #Todavia no encontre ninguna biblioteca para editar el tamano de la imagen segun
        #la resolucion compatible con Python 3.1, y (por alguna razon) el PyScripter no
        #me funciona con Python 3.2 -.-"

        imagenIzquierda=pygame.image.load(IMAGEN_IZQUIERDA+str(NUMERO)+".jpg").convert_alpha()      #Selecciona la imagen Izquierda (Ricky)
        screen.blit(imagenIzquierda,(0, 0)) #Ubica la imagen en la pantalla (Ricky)
        pygame.display.flip()           # ...  (Ricky)

        pygame.mixer.music.load("autos23.mp3")
        sonidoMoneda=pygame.mixer.Sound("bien.wav")
        sonidoMal=pygame.mixer.Sound("mal.wav")
        pygame.mixer.music.play(1)

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        seguirjuego = True

        puntos = 0
        candidata = ""
        listaNombres = []
        posiciones = []
        nombres=[]
        #Agregue estas listas y cadenas (Ricky)
        listaY=[]
        listaX=[]
        distancia=1
        letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        #Esta guarda los nombres del archivo nombres.txt en la cadena nombres (Ricky)
        archivo= open("autos.txt","r")
        for linea in archivo.readlines():
            nombres.append(linea[0:-2])

        jugador = []
        records = []
        try:
            archivo_record = open("records.txt", "rb")
            record = pickle.load(archivo_record)
            archivo_record.close()
        except:
            pass

        dibujar(screen, candidata, listaNombres, posiciones, puntos,segundos, record['nombre'], str(record['puntos']))

        contfps = 0
        while (segundos > fps/1000) and seguirjuego:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 10 #Cambia la de procesamiento (pero genera un titilo molesto) (Ricky)
                #Aumente los fps para mejorar el rendimiento del tipeado (Ricky)

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    seguirjuego = False
                    break

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key,letras)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(candidata, listaNombres, posiciones, nombres,COLOR_LETRAS,listaX,listaY,sonidoMoneda,sonidoMal)

                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000 + diferencia

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)        #Coloca fondo negro detras de la imagen
            screen.blit(imagenIzquierda,(0, 0)) #Modifique la funcion de actualizar la pantalla
            pygame.display.flip()           #para la nueva imagen  (Ricky)





            #Dibujar de nuevo todo
            dibujar(screen, candidata, listaNombres, posiciones, puntos, segundos, record['nombre'], str(record['puntos']))



            pygame.display.flip()

            if contfps==fps: #Mantiene la relacion fps con la bajada de nombres (Ricky)
                actualizar(listaNombres, posiciones, nombres, listaX, listaY, COLOR_LETRAS, distancia)  #Agregue las listas de ejes, color y distancia
                distancia=random.randrange(0,2) #y esta cadena elige aleatoriamente cuando va a aparecer una nueva palabra (Ricky)
                contfps=0 #reinicia contador fps (Ricky)
            contfps+=1 #incrementa contador fps (Ricky)

        pygame.mixer.music.stop()
        if not seguirjuego:
            nosiguejugando()
            salir_del_programa()


        #while 1:
        #    #Esperar el QUIT del usuario
        #    for e in pygame.event.get():
        #        if e.type == QUIT:
        #            pygame.quit()
        #            return

def siguejugando():
    global seguir
    seguir = True
    funcionJuego()
    nuevorecord()
    return

def nosiguejugando():
    global seguir
    seguir = False
    return


def comenzar_nuevo_juego():
    global seguir
    seguir = True
    funcionJuego()
    nuevorecord()
    while seguir:
        continuajugando()

def continuajugando():
    global seguir
    opcionsalir = [
        ("Seguir jugando", siguejugando),
        ("Terminar", nosiguejugando)
        ]
    menu = Menu(opcionsalir)
    while seguir:
        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)
        pygame.display.flip()
        pygame.time.delay(10)
        for e in pygame.event.get():
            continue

def nuevorecord():
    global record
    if int(puntos) > record['puntos']:
        #screen = pygame.display.set_mode((320,240))
        #screen = pygame.display.set_mode((800, 600))
        #fondo = pygame.image.load("maxresdefault.jpg").convert()
        screen.blit(fondo,(0, 0))
        jugador = ask(screen, "New Record! Your Name is? ")
        record['nombre'] = jugador
        record['puntos'] = int(puntos)
        archivo_record = open("records.txt", "wb")
        record = pickle.dump(record, archivo_record)
        archivo_record.close()


def salir_del_programa():
    global salir
    salir = True



def instrucciones():
    print("FunciÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³n que muestra las instrucciones del juego")


if __name__ == '__main__':
    puntos = 0
    record = {'nombre': '', 'puntos': -1}
    salir = False
    seguir = True
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Salir", salir_del_programa),]


    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    fondo = pygame.image.load("maxresdefault.jpg").convert()
    menu = Menu(opciones)


    while not salir:
        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)
        pygame.display.flip()
        pygame.time.delay(10)
        for e in pygame.event.get():
            if e.type == QUIT: ## nro de opcion
                salir_del_programa()
    pygame.quit()


