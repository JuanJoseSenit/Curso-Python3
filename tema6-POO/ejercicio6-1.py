class Pais:
    def __init__(self,nombre,poblacion,area):
        self.__nombre=nombre
        self.__poblacion=poblacion
        self.__area=area
    def getNombre(self):
        return self.__nombre 
    def masGrandeQue(self,elOtroPais):
        if self.__poblacion>elOtroPais.__poblacion:
            return True
        else:
            return False
    def densidadPoblacion(self):
        return round(self.__poblacion/self.__area,0)
    def toString(self):
        print("Nombre: " , self.__nombre , " Poblacion: " , self.__poblacion , "  Area: " , self.__area , " Densidad: " , self.densidadPoblacion())
    
        
    


Espanna=Pais("España",46770000,504645)
Francia=Pais("Francia",66030000,640679)

print(Espanna.masGrandeQue(Francia))
print(Francia.masGrandeQue(Espanna))
print ("La densidad de población de",Espanna.getNombre(),"es de",Espanna.densidadPoblacion(), "habitantes/km2")
print ("La densidad de población de",Francia.getNombre(),"es de",Francia.densidadPoblacion(), "habitantes/km2")

Espanna.toString()
Francia.toString()