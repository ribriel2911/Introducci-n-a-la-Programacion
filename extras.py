# -*- coding: utf-8 -*-
import pygame, string
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key,letras): #Mejore la funcion de dar letra (Ricky)
    if key > 96 and key < 123:
        return letras[key-97]
    elif key==32:
        return (" ")
    else:
        return("")

def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)


def dibujar(screen, candidata, listaNombres, posiciones, puntos, segundos, maximojugador, maximorecord):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    fuenteGTA= pygame.font.Font('fuente2.ttf', 40)

    #Linea del piso
    pygame.draw.line(screen, COLOR_PUNTOS, (0, ALTO-(TAMANNO_LETRA*3)) , (ANCHO, ALTO-(TAMANNO_LETRA*3)), 5)
    pygame.draw.line(screen, COLOR_PUNTOS, (360, 0) , (360, ALTO-(TAMANNO_LETRA*3)), 5)
    #Se mueve segun el tamaÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±o de la letra

    ren1 = defaultFont.render(candidata, 1, COLOR_CANDIDATA)        #Independice los colores de cada uno (Ricky)
    ren2 = fuenteGTA.render(PUNTOS + str(puntos), 1, COLOR_PUNTOS)
    ren4 = fuenteGTA.render("Best Player: " + str(maximojugador), 1, COLOR_PUNTOS)
    ren5 = fuenteGTA.render("Record: " + str(maximorecord), 1, COLOR_PUNTOS)
    if(segundos<15):
        ren3 = fuenteGTA.render(TIEMPO + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = fuenteGTA.render(TIEMPO + str(int(segundos)), 1, COLOR_TIEMPO)

    for i in range(len(listaNombres)):
        screen.blit(defaultFont.render(listaNombres[i], 1, COLOR_LETRAS[i]), posiciones[i]) #Modifique COLOR_LETRAS para que asigne el color a cada nombre (Ricky)

    screen.blit(ren1, ((len(PUNTOS)+1)*TAMANNO_LETRA*RELACION, ALTO-(TAMANNO_LETRA*2)))
    screen.blit(ren2, (10, 10)) #Mejore la relacion con los margenes (Ricky)
    screen.blit(ren3, (10, 10+(TAMANNO_LETRA*2)))
    screen.blit(ren4, (10, 10+(TAMANNO_LETRA*4)))
    screen.blit(ren5, (10, 10+(TAMANNO_LETRA*8)))


def get_key():
    letra = None
    while letra is None:
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                letra = e.key
    return letra

def display_box(screen, message):
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font(None,18)
    pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    300,20), 0)
    pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    304,24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()

def ask(screen, question):
    "ask(screen, question) -> answer"
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + "".join(current_string))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey in (K_RETURN, K_ESCAPE):
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string))
    return "".join(current_string)
