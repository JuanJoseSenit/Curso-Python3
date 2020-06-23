import random

class ElJuegoDeCartas:
    def __init__(self):
        self.palos=["oros","copas","espadas","bastos"]
        self.valores=["dos","tres","cuatro","cinco","seis","siete","sota","caballo","rey","as"]
        self.rondasJugar=5
        self.contadorJugador=0
        self.contadorMaquina=0
    def jugar(self):
        for i in range(self.rondasJugar):
            flag=True
            paloJugador=random.randint(0,len(self.palos)-1)
            numeroJugador=random.randint(0,len(self.valores)-1)
            paloMaquina=random.randint(0,len(self.palos)-1)
            numeroMaquina=random.randint(0,len(self.valores)-1)
            print("RONDA",i+1)
            while numeroJugador==numeroMaquina and paloMaquina==paloJugador:
                paloMaquina=random.randint(0,len(self.palos)-1)
                numeroMaquina=random.randint(0,len(self.valores)-1)
            if numeroJugador>numeroMaquina:
                self.contadorJugador+=1
                print("Tú carta (máquina) es el",self.valores[numeroMaquina],"de",self.palos[paloMaquina],"y la mía el",self.valores[numeroJugador],"de",self.palos[paloJugador],".GANO YO")

            elif numeroMaquina>numeroJugador:
                self.contadorMaquina+=1
                print("Tú carta (máquina) es el",self.valores[numeroMaquina],"de",self.palos[paloMaquina],"y la mía el",self.valores[numeroJugador],"de",self.palos[paloJugador],".GANAS TÚ")
            else:
                print("Tú carta (máquina) es el",self.valores[numeroMaquina],"de",self.palos[paloMaquina],"y la mía el",self.valores[numeroJugador],"de",self.palos[paloJugador],".EMPATAMOS")
            while flag:
                if self.rondasJugar>i+1:
                    comentario=input("pulse una tecla para barajar las cartas")
                flag=False
    def puntuar(self):
        if self.contadorJugador>self.contadorMaquina:
            return [self.contadorMaquina,self.contadorJugador,"GANO YO"]
        elif self.contadorMaquina>self.contadorJugador:
            return [self.contadorMaquina,self.contadorJugador,"GANAS TÚ"]
        else:
            return [self.contadorMaquina,self.contadorJugador,"EMPATAMOS"]


        

""" palos=["oros","copas","espadas","bastos"]
valores=["dos","tres","cuatro","cinco","seis","siete","sota","caballo","rey","as"]
rondasJugar=5
contadorJugador=0
contadorMaquina=0
for i in range(rondasJugar):
    flag=True
    paloJugador=random.randint(0,len(palos)-1)
    numeroJugador=random.randint(0,len(valores)-1)
    paloMaquina=random.randint(0,len(palos)-1)
    numeroMaquina=random.randint(0,len(valores)-1)
    print("RONDA",i+1)
    while numeroJugador==numeroMaquina and paloMaquina==paloJugador:
        paloMaquina=random.randint(0,len(palos)-1)
        numeroMaquina=random.randint(0,len(valores)-1)
    if numeroJugador>numeroMaquina:
        contadorJugador+=1
        print("Tú carta (máquina) es el",valores[numeroMaquina],"de",palos[paloMaquina],"y la mía el",valores[numeroJugador],"de",palos[paloJugador],".GANO YO")

    elif numeroMaquina>numeroJugador:
        contadorMaquina+=1
        print("Tú carta (máquina) es el",valores[numeroMaquina],"de",palos[paloMaquina],"y la mía el",valores[numeroJugador],"de",palos[paloJugador],".GANAS TÚ")
    else:
        print("Tú carta (máquina) es el",valores[numeroMaquina],"de",palos[paloMaquina],"y la mía el",valores[numeroJugador],"de",palos[paloJugador],".EMPATAMOS")
    while flag:
        comentario=input("pulse una tecla para barajar las cartas")
        flag=False


if contadorJugador>contadorMaquina:
    print("RESULTADOS \nMÁQUINA: ",contadorMaquina,"\nYO:",contadorJugador,"\nGANO YO")
elif contadorMaquina>contadorJugador:
    print("RESULTADOS \nMÁQUINA: ",contadorMaquina,"\nYO:",contadorJugador,"\nGANAS TÚ")
else:
    print("RESULTADOS \nMÁQUINA: ",contadorMaquina,"\nYO:",contadorJugador,"\nEMPATAMOS")
 """
    








