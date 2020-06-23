
archivo=open("./prueba.txt","r")

""" lecturaTotal=archivo.read()  #Lee el archivo entero y devuelve un string
lectura=archivo.readline()  #Lee la primera linea y deja el cursor al final de la mima
lectura2=archivo.readline() #Lee la sigiente linea """

lecturaArray=archivo.readlines()    #cada linea del archivo es un valor del array
for i in range(len(lecturaArray)):
    print("linea",i+1,lecturaArray[i])

""" print("Read() devuelve", lecturaTotal, "y es de tipo", type(lecturaTotal))
print(lectura)
print(type(lectura))
print(lectura2) """
print("Readlines() devuelve", lecturaArray, "y es de tipo", type(lecturaArray))


archivo.close()