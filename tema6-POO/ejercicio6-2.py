class Miembro:
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

class Profesor(Miembro):
    def __init__(self,nombre,edad,dni,numRegistro):
        Miembro.__init__(self,nombre,edad,dni)
        self.numRegistro=numRegistro
        self.asignaturasImparte=[]
    def annadeDocencia(self,asignatura):
        self.asignaturasImparte.append(asignatura)
    def imprimeDocencia(self):
        print("--> El profesor",self.nombre,"impartes las asignaturas de:")
    
        for i in range(len(self.asignaturasImparte)):
            print(i+1,self.asignaturasImparte[i].nombre)
            self.asignaturasImparte[i].imprimeListado()

class Estudiante(Miembro):
    def __init__(self,nombre,edad,dni,numEstudiante):
        Miembro.__init__(self,nombre,edad,dni)
        self.numEstudiante=numEstudiante

class Asignatura:
    def __init__(self,nombre,codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.estudiantes=[]
    def annadeEstudiante(self,estudiante):
        self.estudiantes.append(estudiante)
    
    def imprimeListado(self):
        print("La asignatura de", self.nombre,"es cursada por: ")
        for j in range(len(self.estudiantes)):
            print(self.estudiantes[j].nombre)

profe1=Profesor("Luis",50,"34567",5001)
profe2=Profesor("Pepe",37,"65432",5010)

estudiante1=Estudiante("Jorgito",20,"56678",1001)
estudiante2=Estudiante("Juanito",19,"44444",1002)
estudiante3=Estudiante("Jaimito",19,"22334",1005)

asignatura1=Asignatura("Matematicas",5)
asignatura2=Asignatura("Física",7)
asignatura3=Asignatura("Latín",13)
asignatura4=Asignatura("Historia",19)
asignatura5=Asignatura("Filosofía",36)

profe1.annadeDocencia(asignatura1)
profe1.annadeDocencia(asignatura2)
profe2.annadeDocencia(asignatura3)
profe2.annadeDocencia(asignatura4)
profe2.annadeDocencia(asignatura5)

asignatura1.annadeEstudiante(estudiante1)
asignatura2.annadeEstudiante(estudiante2)
asignatura2.annadeEstudiante(estudiante3)
asignatura3.annadeEstudiante(estudiante1)
asignatura3.annadeEstudiante(estudiante3)
asignatura4.annadeEstudiante(estudiante2)
asignatura4.annadeEstudiante(estudiante3)
asignatura5.annadeEstudiante(estudiante3)

profe1.imprimeDocencia()
profe2.imprimeDocencia()

def mostrarAsignaturas(nombreEstudiante):
    listaAsignaturas=[asignatura1,asignatura2,asignatura3,asignatura4,asignatura5]
    print("El estudiante",nombreEstudiante,"cursa las asignaturas de: ")
    for i in range(len(listaAsignaturas)):
        for j in range(len(listaAsignaturas[i].estudiantes)):
            if listaAsignaturas[i].estudiantes[j].nombre==nombreEstudiante:
                print(listaAsignaturas[i].nombre )

mostrarAsignaturas(estudiante1.nombre)






