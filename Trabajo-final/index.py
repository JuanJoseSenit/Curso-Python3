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

from TrabajoFinal import *

matrizPalabrasUtiles = transformarDiccionario()
lecturaArchivoEncriptado=lecturaTextoEncriptado("./fichero_cifrado.txt")  #<--- INTRODUZCA EL FICHERO A DESENCRIPTAR
matrizConvertidaNumero=convertirNumero(lecturaArchivoEncriptado)
listaFinal=escribirArchivo("./fichero_plano.txt",matrizConvertidaNumero,matrizPalabrasUtiles) 
escrituraClaveTextoCorrecto(listaFinal[0],listaFinal[1],listaFinal[2])