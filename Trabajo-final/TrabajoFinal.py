"""
--------------------------------------DATOS-----------------------------------------------
NOMBRE: JUAN JOSÉ
APELLIDOS: SENIT VELASCO
MODALIDAD: Propuesta 2: "Hackeando, a lo bruto, a lo Julio César"
No han sido usadas bibliotecas "extra"
NOTAS: El trabajo dispone de dos ficheros .py (TrabajoFinal.py e index.py)
    index.py: El que hay que ejecutar. Contiene las llamadas a las funciones necesarias
    TrabajoFinal.py: Contiene las funciones (lógica del programa)
------------------------------------------------------------------------------------------
"""

#Función que lee Diccionario.txt y cada palabra(que se encuentra en una linea) es almacenada en una lista
def transformarDiccionario():
    archivoDiccionario=open("./Diccionario.txt","r",encoding='ISO-8859-1')
    #diccionario contiene una lista con todas las palabras
    diccionario=archivoDiccionario.readlines() 
    archivoDiccionario.close()
    #matrizPalabrasUtiles va a almacenar las palabras de diccionario con los cambios necesarios
    matrizPalabrasUtiles=[] 
    #bucle que recorre diccionario y aplica los cambios deseados
    for i in range(len(diccionario)):
        palabra=diccionario[i].upper()
        palabra=palabra.replace("Ñ","NN")
        palabra=palabra.replace("Á","A")
        palabra=palabra.replace("É","E")
        palabra=palabra.replace("Í","I")
        palabra=palabra.replace("Ó","O")
        palabra=palabra.replace("Ú","U")
        palabra=palabra.replace("Ü","U")
        #se almacenan las palabras de 4 caracteres en adelante para, a la hora de buscar estas palabras en cada uno de los códigos, evitar falsos positivos
        if len(palabra)>3:
            matrizPalabrasUtiles.append(palabra)
    return matrizPalabrasUtiles
    
#Función que lee el fichero encriptado
def lecturaTextoEncriptado(nombre_fichero):
    archivoEncriptado=open(nombre_fichero,"r")
    lecturaArchivoEncriptado=archivoEncriptado.read()
    archivoEncriptado.close()
    lecturaArchivoEncriptado=lecturaArchivoEncriptado.upper()
    lecturaArchivoEncriptado=lecturaArchivoEncriptado.replace(" ", "")
    return lecturaArchivoEncriptado

#Función que convierte el archivo encriptado a número (según el código ASCII)
def convertirNumero(lecturaArchivoEncriptado):
    matrizConvertidaNumero=[]
    #bucle que recorre la cadena de texto encriptada
    for i in range(len(lecturaArchivoEncriptado)):
        #ord()permite transformar la letra por el número que le corresponde en ASCII. Como la A es el 65, y de ahí en adelante, se le
        #resta 65 para ponerlo en base 0
        matrizConvertidaNumero.append(ord(lecturaArchivoEncriptado[i])-65)
    return matrizConvertidaNumero

#Función que muestra por pantalla los resultados de desencriptar, además de comprobar cual es la clave correcta
def escribirArchivo(fichero_escritura,matrizConvertidaNumero,matrizPalabrasUtiles):
    matrizFinalCadenasconenne=[]
    aux=0
    archivoEscritura=open(fichero_escritura,"w")
    print("Bucle de crackeo:")
    #bucle for que recorre cada una de las claves
    for i in range(26):
        contador=0
        resultadoCadena=""
        #bucle for anidado que recorre cada clave y pasa de números a letras
        for j in range(len(matrizConvertidaNumero)):
            #numero es el número de cada posición del array+i, ya que a cada vuelta de i, la clave se incrementa en 1, y por tanto el número también
            #Nos quedamos con el resto
            numero=(matrizConvertidaNumero[j]+i)%26
            #Cambiamos a letra
            letra=chr(numero+65)
            #ResultadoCadena contiene cada string para cada código, con la Ñ como NN
            resultadoCadena=resultadoCadena+letra
        #resultadoCadena2 sustituye para cada resultadaCadena la NN por Ñ (que es lo que vamos a mostrar)
        resultadoCadena2=resultadoCadena.replace("NN","Ñ")  #me creo una variable con la cadena pasada a Ñ
        
        #Bucle que recorre el diccionario buscando coincidencias con cada una de las cadenas
        #IMPORTANTE: Se usa resultadaCadena y no resultadoCadena2 porque matrizPalabrasUtiles es el diccionario que contiene NN en lugar
        #de Ñ (ver función TransformacionDiccionario)
        for n in range(len(matrizPalabrasUtiles)):
            #hay que eliminar los saltos de linea para cada elemento de la lista
            matrizPalabrasUtiles[n]=matrizPalabrasUtiles[n].replace("\n", "")
            if matrizPalabrasUtiles[n] in resultadoCadena:  
                contador=contador+resultadoCadena.count(matrizPalabrasUtiles[n])   
        #Almaceno en una lista cada una de las cadenas que corresponden a cada clave
        matrizFinalCadenasconenne.append(resultadoCadena2)
        if contador > aux:
            aux = contador
            clave=i
        #El siguiente bloque de código escribe en el fichero específico
        numeracion= str(i)+ " "
        archivoEscritura.write(numeracion)
        archivoEscritura.write(resultadoCadena2)  # a la hora de escribir meto las que tienen Ñ
        archivoEscritura.write("\n")
        print(i,"  ",resultadoCadena2,"\n")
    #En el return devuelvo un lista que contiene un array, la clave y en archivo escrito que son necesarios para la siguiente función
    return [matrizFinalCadenasconenne,clave,archivoEscritura]    

#Función que escribe la clave más probable y la cadena correspondiente a dicha clave
def escrituraClaveTextoCorrecto(matrizFinalCadenasconenne,clave,archivoEscritura):
    archivoEscritura.write("La clave mas probable es: ")
    archivoEscritura.write(str(clave))
    archivoEscritura.write("\nQue se corresponde a: \n")
    archivoEscritura.write(matrizFinalCadenasconenne[clave])
    print("La clave más probable es:", clave, matrizFinalCadenasconenne[clave])
    archivoEscritura.close()







    









    


    
    

