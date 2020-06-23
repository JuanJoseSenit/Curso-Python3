def calcularDivisor(num):
    matrizDivisores=[]
    print("Los divisores de",num,"(sin almacenarlos) son: ")
    for i in range(1,num+1):
        if num%i==0:
            print(i)
            matrizDivisores.append(i)
    return matrizDivisores
    
flag=True
while flag==True:
    try:
        numero=input("Introduzca el número del cual desea saber sus divisores")
        matrizDivisores=calcularDivisor(int(numero))
    except KeyboardInterrupt:
        print("\nHas interrumpido la ejecución del programa")
        flag=False
    except ValueError:
        print("Recuerde que debe introducir números")
    else:
        print("Los divisores de",numero, "(almacenados, y por lo tanto accesibles para operar con ellos) son: ",matrizDivisores)
        flag=False
    






