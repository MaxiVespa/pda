class UC:
    def __init__(self,nombre:str,code:str,ucregulares:list, ucaprobadas:list, semestre:int, creditos:int)->None:
        self.nombre=nombre
        self.code=code
        self.ucregulares=ucregulares
        self.ucaprobadas=ucaprobadas
        self.semestre=semestre
        self.creditos=creditos
    #Metodos
    def getAtributos(self):
        return [self.nombre,self.code,self.ucregulares,self.ucaprobadas,self.semestre,self.creditos]

#Plan tecnólogo 
#Semestere 1
############################################################################################################
S1UC1 = UC(nombre = "Álgebra , Análisis y Geometría Analítica", code = 'S1UC1',ucregulares = [], ucaprobadas = [], semestre  = 1, creditos = 8)

S1UC2  = UC(nombre ="Mecanica, Ondas y Calor " , code ='S1UC' , ucregulares = [] , ucaprobadas = [] , semestre  =1 , creditos = 10 )

S1UC3 = UC(nombre = "Química General e inorgánica" , code = 'S1UC3' , ucregulares =[] , ucaprobadas =[] , semestre  = 1 , creditos = 9 )

S1UC4 = UC(nombre ="Taller Inicial de Tecnologías (Anual)" , code = 'S1UC4' , ucregulares =[] , ucaprobadas = [], semestre  = 1, creditos = [] )

S1UC5 = UC(nombre ="Salud y Sociedad" , code ='S1UC5' , ucregulares =[] , ucaprobadas =[] , semestre  = 1, creditos =8 )

S1UC6 = UC(nombre ="Programas Especiales" , code ='S1UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 1, creditos =2 )

S1UC7 = UC(nombre = "Inglés 1" , code ='S1UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 1, creditos =4 )

#Semestere 2
############################################################################################################
S2UC1 = UC(nombre = "Números Complejos y Ecuaciones Diferenciales", code = 'S2UC1', ucregulares = [S1UC1.code], ucaprobadas = [], semestre  = 2, creditos = 8)

S2UC2  = UC(nombre ="Electricidad y Magnetismo " , code ='S2UC' , ucregulares = [S1UC1.code,S1UC2.code] , ucaprobadas = [] , semestre  =2 , creditos = 10 )

S2UC3 = UC(nombre = "Química Orgánica y Biológica" , code = 'S2UC3' , ucregulares =[S1UC3.code] , ucaprobadas =[] , semestre  = 2 , creditos = 9 )

S2UC4 = UC(nombre ="Taller Inicial de Tecnologías (Anual)" , code = 'S2UC4' , ucregulares =[] , ucaprobadas = [], semestre  = 2, creditos = 8 )

S2UC5 = UC(nombre ="Anatomía y Fisiologia Humanas" , code ='S2UC5' , ucregulares =[S1UC1.code,S1UC5.code] , ucaprobadas =[] , semestre  = 2, creditos =8 )

S2UC6 = UC(nombre ="Programas Especiales" , code ='S2UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 2, creditos =2 )

S2UC7 = UC(nombre = "Inglés 2" , code ='S2UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 2, creditos = 4 )

#Semestere 3
############################################################################################################
S3UC1 = UC(nombre = "Ópticas y Radiaciones", code = 'S3UC1', ucregulares = [S1UC1.code,S1UC2.code], ucaprobadas = [], semestre  = 3, creditos = 10)

S3UC2  = UC(nombre ="Electrónica Analógica " , code ='S3UC' , ucregulares = [S2UC1.code,S2UC2.code,S2UC4.code] , ucaprobadas = [S1UC1,S1UC2] , semestre  =3 , creditos = 10 )

S3UC3 = UC(nombre = "Electrotecnia" , code = 'S3UC3' , ucregulares =[S2UC1,S2UC2] , ucaprobadas =[] , semestre  = 3 , creditos = 9 )

S3UC4 = UC(nombre ="Instalaciones Hospitalarias" , code = 'S3UC4' , ucregulares =[S1UC3.code,S2UC5.code,S2UC2.code] , ucaprobadas = [S1UC1.code,S1UC5.code,S1UC2.code], semestre  = 3, creditos = 9 )

S3UC5 = UC(nombre ="Programación de Computadoras" , code ='S3UC5' , ucregulares =[S1UC1.code] , ucaprobadas =[] , semestre  = 3, creditos =8 )

S3UC6 = UC(nombre ="Programas Especiales" , code ='S3UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 3, creditos =2 )

S3UC7 = UC(nombre = "Inglés 3" , code ='S3UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 3, creditos = 4 )

#Semestere 4
############################################################################################################
S4UC1 = UC(nombre = "Electrofisiología Clinica", code = 'S4UC1', ucregulares = [S2UC5.code,S3UC2.code], ucaprobadas = [S1UC1.code,S1UC5.code,S2UC1.code,S2UC2.code,S2UC4.code], semestre  = 4, creditos = 10)

S4UC2  = UC(nombre ="Electrónica Digital" , code ='S4UC' , ucregulares = [S3UC2.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S2UC4.code] , semestre  = 4 , creditos = 10 )

S4UC3 = UC(nombre = "Mecánica Maquinas y Materíales" , code = 'S4UC3' , ucregulares =[S1UC1.code,S1UC2.code] , ucaprobadas = [] , semestre  = 4 , creditos = 9 )

S4UC4 = UC(nombre ="Imagenes Médicas" , code = 'S4UC4' , ucregulares =[S2UC5.code,S3UC1.code] , ucaprobadas = [S1UC1.code,S1UC5.code,S1UC2.code], semestre  = 4, creditos = 10 )

S4UC5 = UC(nombre ="Práctica Profesional Curriculas A(PPC A) - Internado Rotatorio - Anual" , code ='S4UC5' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] , ucaprobadas =[] , semestre  = 4, creditos = [] )

S4UC6 = UC(nombre ="Programas Especiales" , code ='S4UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 4, creditos =2 )

S4UC7 = UC(nombre = "Inglés 4" , code ='S4UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 4, creditos = 4 )

#Semestere 5
############################################################################################################
S5UC1 = UC(nombre = "Seguridad Eléctrica y Radiante", code = 'S5UC1', ucregulares = [S3UC3.code,S3UC4.code,S4UC1.code,S4UC4.code], ucaprobadas = [S1UC1.code,S1UC3.code,S2UC5.code,S2UC2.code,S3UC1.code], semestre  = 5, creditos = 10)

S5UC2  = UC(nombre ="Normativa sobre Equipamiento Médico" , code ='S5UC' , ucregulares = [S3UC3.code,S3UC4.code,S4UC1.code,S4UC3.code,S4UC4.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S1UC1.code,S1UC2.code,S3UC1.code] , semestre  = 5 , creditos = 8 )

S5UC3 = UC(nombre = "Taller de Mantenimiento de Equipos Médicos" , code = 'S5UC3' , ucregulares =[S3UC3.code,S3UC4.code,S4UC1.code,S4UC3.code,S4UC4.code] , ucaprobadas =[S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S1UC1.code,S1UC2.code,S3UC1.code] , semestre  = 5 , creditos = 10 )

S5UC4 = UC(nombre ="Matemática Avanzada I" , code = 'S5UC4' , ucregulares =[S2UC1.code,S3UC5.code] , ucaprobadas = [S1UC1.code], semestre  = 4, creditos = 9 )

S5UC5 = UC(nombre ="Práctica Profesional Curriculas A(PPC A) - Internado Rotatorio - Anual" , code ='S4UC5' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] ,  ucaprobadas =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code] , semestre  = 4, creditos = 12)

S5UC6 = UC(nombre ="Programas Especiales" , code ='S5UC6' , ucregulares =[] , ucaprobadas =[] , semestre  = 5, creditos =2 )

S5UC7 = UC(nombre = "Inglés 5" , code ='S5UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 5, creditos = 4 )

#Semestere 6
############################################################################################################
S6UC1 = UC(nombre = "Instrumental de Laboratorio Clinico", code = 'S6UC1', ucregulares = [S2UC3.code,S3UC4.code], ucaprobadas = [S1UC3.code,S2UC5.code,S2UC2.code], semestre  = 6, creditos = 9)

S6UC2  = UC(nombre ="Informatica Médica" , code ='S6UC' , ucregulares = [S3UC3.code,S4UC1.code,S4UC4.code] , ucaprobadas = [S2UC1.code,S2UC2.code,S2UC5.code,S3UC2.code,S3UC1.code] , semestre  = 6 , creditos = 8 )

S6UC3 = UC(nombre = "Instrumentación Médica Complementaria" , code = 'S6UC3' , ucregulares =[S3UC3.code,S3UC4.code,S4UC1.code,S4UC4.code] , ucaprobadas =[S2UC1.code,S2UC2.code,S1UC3.code,S2UC5.code,S3UC2.code,S3UC1.code] , semestre  = 6 , creditos = 10 )

S6UC4 = UC(nombre ="Matemática Avanzada II" , code = 'S6UC4' , ucregulares =[S5UC4.code] , ucaprobadas =[S2UC1.code,S3UC5.code], semestre  = 6, creditos = 9 )

S6UC5 = UC(nombre ="Fisíca Avanzada " , code ='S6UC5' , ucregulares =[S3UC1.code,S3UC3.code] , ucaprobadas =[S1UC1.code,S1UC2.code,S2UC1.code,S2UC2.code] , semestre  = 6, creditos =8 )

S6UC6 = UC(nombre ="PT Proyecto Final de Titulación"  , code ='S6UC6' , ucregulares =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code, S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code, S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code,
S4UC1.code,S4UC2.code,S4UC3.code,S4UC4.code,S4UC5.code,S4UC6.code,S4UC7.code, S5UC1.code,S5UC2.code,S5UC3.code,S5UC4.code,S5UC5.code,S5UC6.code,S5UC7.code] , ucaprobadas =[S1UC1.code,S1UC2.code,S1UC3.code,S1UC4.code,S1UC5.code,S1UC6.code,S1UC7.code,
S2UC1.code,S2UC2.code,S2UC3.code,S2UC4.code,S2UC5.code,S2UC6.code,S2UC7.code,
S3UC1.code,S3UC2.code,S3UC3.code,S3UC4.code,S3UC5.code,S3UC6.code,S3UC7.code,
S4UC1.code,S4UC2.code,S4UC3.code,S4UC4.code,S4UC5.code,S4UC6.code,S4UC7.code,
S5UC1.code,S5UC2.code,S5UC3.code,S5UC4.code,S5UC5.code,S5UC6.code,S5UC7.code,] , semestre  = 6, creditos = 8  )

S6UC7= UC(nombre ="Programas Especiales" , code ='S6UC7' , ucregulares =[] , ucaprobadas =[] , semestre  = 6, creditos =2 )

S6UC8 = UC(nombre = "Inglés 6" , code ='S6UC8' , ucregulares =[] , ucaprobadas =[] , semestre  = 6, creditos = 4 )

#######################################################


class IBIO2019():
    def __init__(self,*unidadCurricular:UC) -> None:
        self.unidadCurricular=unidadCurricular
    
    def getUCplan2019(self):
        plan=[]        
        for i in range(0,len(self.unidadCurricular)):
            plan.append(self.unidadCurricular[i].code)
        return plan

    def getSemestre(self,numSemestre:int): #OBTENER MATERIAS POR SEMESTRES
        semestre1=[]        
        for i in range(0,len(self.unidadCurricular)):
            if self.unidadCurricular[i].semestre==numSemestre:
                semestre1.append(self.unidadCurricular[i].code)
        return semestre1
    
#plan2019 = [S1UC1,S1UC2,S1UC3,S1UC4,S1UC5,S1UC6,S1UC7,S2UC1,S2UC2,S2UC3,S2UC4,S2UC5,S2UC6,S2UC7,S3UC1,S3UC2,S3UC3,S3UC4,S3UC5,S3UC6,S4UC7,S4UC1,S4UC2,S4UC3,S4UC4,S4UC5,S4UC6,S4UC7,S5UC1,S5UC2,S5UC3,S5UC4,S5UC5,S5UC6,S5UC7,S6UC1,S6UC2,S6UC3,S6UC4,S6UC5,S6UC6,S6UC7,S6UC8]
   
class Persona():
    def __init__(self,nombrePersona:str, apellidos:str, CI:int, edadPersona:int):
        self.nombrePersona=nombrePersona
        self.apellidos=apellidos
        self._CI=CI        
        self.edadPersona=edadPersona      
    
    #Metodos

class Estudiantes(Persona):
    def __init__(self, nombrePersona: str, apellidos: str, CI: int, edadPersona: int, aIngreso:int,ucinscripta=[],ucregulares=[],ucaprobadas=[]):
        super().__init__(nombrePersona, apellidos, CI, edadPersona)
        self.aIngreso=aIngreso
        self._accCode=3
        self.ucaprobadas=ucaprobadas
        self.ucregulares=ucregulares
        self.ucinscripta=ucinscripta
    #Metodos
    
    #metodo para insicpcion a UC con consdicion segun orevias y regulares
    def ucInscriptas(self):

        return self.ucinscripta
    def __str__(self) -> str:
        return super().__str__()

class Secetaria(Persona):
    def __init__(self, nombrePersona: str, apellidos: str, CI: int, edadPersona: int):
        super().__init__(nombrePersona, apellidos, CI, edadPersona)
        self._accCode=2

    #Metodos

class Coridnadora(Persona):
    def __init__(self, nombrePersona: str, apellidos: str, CI: int, edadPersona: int):
        super().__init__(nombrePersona, apellidos, CI, edadPersona)
        self._accCode=1

    #Metodos

def main():
    """ impelmentacion"""
    print(semestre1=unidadesCurriculares(1))
    
if __name__ == '__main__':
    main()

###FUNCIONES####

def inscripcionUCtodos(usuario, codigoAcceso,UC):
        if codigoAcceso==3:    
            if UC in usuario.ucinscripta:
                print("Estudiante ya esta inscripto en esta UC")
            elif UC.ucregulares == usuario.ucregulares or UC.ucaprobadas == usuario.ucaprobadas:
                usuario.ucinscripta.append(UC)
                print("Inscripto en esta UC")
            else:
                print("no se puede")
            