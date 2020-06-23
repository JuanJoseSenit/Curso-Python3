
numeroBinario=input("Introduzca número binario: ")

comprobacion=False
while comprobacion==False:
    comprobacion=True
    for i in range(len(numeroBinario)):
        if numeroBinario[i]!="0" and numeroBinario[i]!="1":
            comprobacion=False
            break
    if comprobacion==False:
        numeroBinario=input("Un número binario está compuesto por 0 y 1: ")

numeroDecimal=0
j=0
for i in range(len(numeroBinario)-1,-1,-1):
    if numeroBinario[i]=="1":
        numeroDecimal=numeroDecimal+2**j
    j+=1

print("El número binario "+ numeroBinario+" tiene un valor en decimal de: " +str(numeroDecimal)) 


""" SEGUNDA FORMA. INVIRTIENDO EL STRING"""

""" numeroBinarioInvertido = numeroBinario[::-1]
numeroDecimal=0
for i in range(len(numeroBinarioInvertido)):
    if numeroBinarioInvertido[i]=="1":
        numeroDecimal=numeroDecimal+2**i

print("El número binario "+ numeroBinario+" tiene un valor en decimal de: " +str(numeroDecimal)) """




