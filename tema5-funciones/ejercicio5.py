""" CALCULO DEL FACTORIAL DE FORMA ITERATIVA """

def fact_i(num):
    numerofactorial=1
    if num==1 or num==0:
        return 1
    for i in range(1,num+1):
        numerofactorial=numerofactorial*i
    return numerofactorial

def fact_i2(num):
    numerofactorial=1
    if num==1 or num==0:
        return 1
    while num>=1:
        numerofactorial=numerofactorial*num
        num=num-1
    return numerofactorial

"""CALCULO DEL FACTORIAL DE FORMA RECURSIVA"""

def fact_r(num):
    if num==1 or num==0:
        return 1
    return num*fact_r(num-1)


numero=input("Introduzca un número: ")

while numero.isnumeric()==False or int(numero)<0:
    numero=input("Por favor, un número mayor o igual que 0")

print("ITERATIVA con bucle for: El factorial de " + numero+" es " +str(fact_i(int(numero))))
print("ITERATIVA con bucle while: El factorial de " + numero+" es " +str(fact_i2(int(numero))))
print("RECURSIVA: El factorial de " + numero+" es " +str(fact_r(int(numero))))
