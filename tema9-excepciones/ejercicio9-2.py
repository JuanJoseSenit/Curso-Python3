import random

class JuegoAdivinar:
    def __init__(self):
        self.numeroAleatorio=random.randint(0,10)
        self.contador=3
        #Pasa saber el número aleatorio a adivinar, descomentar la linea 8
        #print("Número a adivinar",self.numeroAleatorio)  
      
    def jugar(self):
        flag2=True
        while flag2:
            try:  
                self.numeroIntroducido=int(input("Introduzca un número del 0 al 10 (ambos incluidos)"))
                flag=True
                if self.numeroIntroducido==self.numeroAleatorio and self.contador==3:
                    return "Ha acertado a la primera!!"
                else:
                    while self.numeroAleatorio!=self.numeroIntroducido:        
                        if self.contador>1:
                            self.contador-=1
                            print("Ha fallado. Le quedan",self.contador,"intentos")
                            self.numeroIntroducido=int(input("Introduzca otro número: "))    
                        else:
                            flag=False
                            break

                    if flag==True:
                        return "Ha ganado"
                    else:
                        return "Ha perdido"
            except KeyboardInterrupt:
                return "\nHas interrumpido la ejecución del programa"
            except ValueError:
                self.contador-=1
                print("Recuerde que deben ser números. Le quedan",self.contador,"intentos")
            
juego1=JuegoAdivinar()
print(juego1.jugar())
