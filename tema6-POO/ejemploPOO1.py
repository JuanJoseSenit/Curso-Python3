""" Crear la clase Persona con los atributos edad y
nombre.
Crear el método cumpleaños, que incrementa la edad en 1. """

class Persona:
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre

    def cumplir_años(self):
        return self.edad+1

persona1=Persona(20,"Pepe")

print("La edad de " +persona1.nombre+ " es de "+ str(persona1.edad))
print("Dentro de 5 días será su cumple, y tendrá " + str(persona1.cumplir_años()))
