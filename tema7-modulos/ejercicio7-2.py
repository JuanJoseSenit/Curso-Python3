import calendar

class DiaPrevisto:
    def __init__(self,anno,mes,dia):
        self.anno=anno
        self.mes=mes
        self.dia=dia
        
    def calcularDiaSemana(self):
        listaDiaSemana=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
        diaSemana=calendar.weekday(self.anno,self.mes,self.dia)
        
        for i in range(len(listaDiaSemana)):
            if i==diaSemana:
                return listaDiaSemana[i]
                break

    def getMes(self):
        meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septuembre","Octubre","Noviembre","Diciembre"]
        return meses[self.mes-1]

    def toString(self):
        print("El día",self.dia,"de",self.getMes(),"del año",self.anno,"será",self.calcularDiaSemana())


diaSemana1=DiaPrevisto(2025,2,19)
diaSemana1.toString()
