from utec import Estudiantes,Secetaria,UC,IBIO2019,Coridnadora, inscripcionUCtodos
import utec

alumno3=Estudiantes("Martin","Machado",43471650,31,2018,[utec.S1UC2,utec.S1UC3,utec.S1UC4,utec.S1UC5,utec.S1UC6])
# print(S4UC5.getAtributos())
# plan=IBIO2019(S1UC1,S1UC2,S1UC3,S1UC4,S1UC5,S1UC6,S1UC7,S2UC1,S2UC2,S2UC3,S2UC4,S2UC5,S2UC6,S2UC7,S3UC1,S3UC2,S3UC3,S3UC4,S3UC5,S3UC6,S4UC7,S4UC1,S4UC2,S4UC3,S4UC4,S4UC5,S4UC6,S4UC7,S5UC1,S5UC2,S5UC3,S5UC4,S5UC5,S5UC6,S5UC7,S6UC1,S6UC2,S6UC3,S6UC4,S6UC5,S6UC6,S6UC7,S6UC8)
# print(plan.getUCplan2019())
inscripcionUCtodos(alumno3,alumno3._accCode,utec.S2UC1)
#print(alumno1.ucinscripta)
#smestre1= plan.getSemestre(1)#entrega el plan de estudio dicriminado por semestre
#print(smestre1)
# print(len(smestre1))
# print(alumno1.inscripcionUC(S1UC1))
# print(alumno1.ucInscriptas())