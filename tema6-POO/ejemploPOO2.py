""" Crear una clase, Volumen, que sea el control de
volumen de un reproductor de música: con el atributo
del nivel de volumen, nivel, y con los métodos que
definen lo que podemos hacer: subir, bajar o
silenciar el volumen.
- Al poner en marcha el reproductor de música el volumen se
situará en el nivel 3.
- Con los botones de subir o bajar el nivel aumentará o
disminuirá de 1 en 1.
- El botón silenciar situará el nivel en el 0.
- El volumen no podrá superar el nivel 10, si se intenta subir
permanecerá igual.
- El volumen no podrá bajar del nivel 0, si se intenta bajar
permanecerá igual.
- Cada vez que se accione un botón se mostrará en pantalla el
nivel de volumen. """

class Volumen:
    def __init__(self):
        self.nivel=3
    def subir(self):
        if self.nivel>=10:
            print("No se puede subir más el volumen")
        else:
            self.nivel=self.nivel+1
            print("Nivel de sonido: " + str(self.nivel))
    def bajar(self):
        if self.nivel<=0:
            print("No puedes bajar más el volumen")
        else:
            self.nivel=self.nivel-1
            print("Nivel de sonido: " + str(self.nivel))
    def silenciar(self):
        self.nivel=0
        print("Muteado. Nivel de sonido a 0")


radio=Volumen()

radio.subir()
radio.bajar()
radio.bajar()
radio.bajar()
radio.bajar()
radio.bajar()
radio.bajar()
radio.subir()
radio.subir()
radio.subir()
radio.silenciar()