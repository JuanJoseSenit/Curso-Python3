from juegoCartas import *

juego1=ElJuegoDeCartas()
juego1.jugar()
resultado=juego1.puntuar()
print("RESULTADO \nMÁQUINA:",resultado[0],"\nYO:",resultado[1],"\n",resultado[2])