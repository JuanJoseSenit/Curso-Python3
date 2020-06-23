archivoLeer=input("Introduzca el nombre del archivo al que desea hacer un backup")

#------------1 FORMA: LECTURA LINEA A LINEA--------------------

archivoBackup=open("./bak.txt","w")
archivo=open("./"+archivoLeer,"r")

linea="inicio"
while linea!="":

    linea=archivo.readline()
    archivoBackup.write(linea)
   

#------------2 FORMA: RECORRIENDO EL ARRAY DE LINEAS-----------------

"""archivoBackup=open("./bak.txt","w")
archivo=open("./"+archivoLeer,"r")

lecturaArray=archivo.readlines()
for i in range(len(lecturaArray)):
  
    archivoBackup.write(lecturaArray[i])"""

archivoBackup.close()
archivo.close()






