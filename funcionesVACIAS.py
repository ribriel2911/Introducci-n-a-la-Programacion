from configuracion import *

import random
import math


def color(candidata):
    if Puntos(candidata)>=30:
        color=(255,0,0)
    else:
        if Puntos(candidata)>=15:
            color=(0,0,255)
        else:
            color=(0,255,0)
    return color

def actualizar(listaNombres, posiciones, nombres, listaX, listaY, colores,distanciador):        #Listo
    for indice in range(len(listaNombres)): #Recorre la lista de nombres por indice
        listaY[indice]+=((TAMANNO_LETRA*RELACION)+5)  #Toma el Y guardado en cada indice y lo incrementa
        posiciones[indice]=(listaX[indice],listaY[indice]) #Hace bajar las palabras cambiando el Y por el nuevo
    if distanciador==1:             #Deside al azar cuando aparecera la siguiente palabra
        nombre=nuevoNombre(nombres)     #Crea un nuevo nombre
        listaNombres.append(nombre)     #Agrega el nuevo nombre a la lista
        limite=int(ANCHO-(len(nombre)*TAMANNO_LETRA*RELACION))  #Marca limite derecho de la pantalla
        x=random.randrange(365,limite)  #Ubica el X en una posicion aleatoria
        listaX.append(x)    #Guarda el eje X nuevo
        listaY.append(5)    #Crea un eje Y nuevo y lo guarda
        posiciones.append((listaX[len(listaNombres)-1],listaY[len(listaNombres)-1])) #Guarda la posicion de la palabra nueva
        colores.append(color(nombre))#Designa el color
    if len(listaY)>1:   #No hace nada si ya se borraron todas las palabras
        if listaY[0]+(TAMANNO_LETRA*RELACION)>=ALTO-(TAMANNO_LETRA*3):  #Borra las palabras que bajan de la pantalla
            listaNombres.pop(0)
            posiciones.pop(0)
            listaX.pop(0)
            listaY.pop(0)
            colores.pop(0)
    return()




def estaCerca(elem, lista):         #No la usamos
    for g in lista:
        if(elem==g):
            return False
    return True

def nuevoNombre(nombres):                           #Listo
    azar=random.randrange(len(nombres))
    otroNombre=nombres[azar].upper()
    return otroNombre


def quitar(candidata, listaNombres, posiciones,colores,listaX,listaY):      #Listo
    i=0
    while(i<(len(listaNombres))):
        if(candidata==listaNombres[i]):
            listaNombres.pop(i)
            posiciones.pop(i)
            colores.pop(i)
            listaX.pop(i)
            listaY.pop(i)
        i+=1
    return()

def esValida(candidata, listaNombres):              #Listo
    flag=False
    for nombre in listaNombres:
        if candidata==nombre:
            flag=True
    return flag


def Puntos(candidata):              #Listo
    CantidadPuntos=0
    for char in candidata:
        if(char=="a" or char=="e" or char=="i" or char=="o" or char=="u"):
            CantidadPuntos+=1
        else:
                if(char=="j" or char=="k" or char=="q" or char=="w" or char=="x" or char=="y" or char=="z"):
                    CantidadPuntos+=5
                else:
                        CantidadPuntos+=2
    return CantidadPuntos


def procesar(candidata, listaNombres, posiciones,nombres,colores,listaX,listaY,sonidoMoneda,sonidoMal):
    puntaje=0
    if esValida(candidata,listaNombres):
        quitar(candidata,listaNombres,posiciones,colores,listaX,listaY)
        puntaje=puntaje+Puntos(candidata)
        sonidoMoneda.play()
    else:
        sonidoMal.play()
    return puntaje

