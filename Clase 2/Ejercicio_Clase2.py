#Programa de promedios:
#Ingresar nombre y apellido de un alumno y sus notas de matematica, literatura, y fisica
#Se pide Imprimir el nombre y el apellido
# si el promedio es mayor a 6 entonces debe aparecer un cartel que diga 'Aprobado'
# si tiene menos de 4 puntos imprimir 'Insuficiente'
# si tiene entre 4 y 5,999999 imprimir 'A recuperatorio'
# En caso de tener 9 o mas imprimir - a parte de aprobado 'Alumno destacado'

#como hacer para que la nota no pueda ser > a 10 ?

def imp_promedio(nom, ape, mat, lit, fis):
    estado =""
    destacado=""

    if ((int(mat) <11) and (int(lit)<11) and (int(fis)<11)):
        prom = ((int(mat) + int(lit) + int(fis)) /3)
        if prom < 4:
            estado="Insuficiente"
        elif prom > 4 and prom < 6:
            estado ="A recuperatorio"
        elif prom>6:
            estado="Aprobado "
            if prom>=9:
                destacado="Alumno destacado"
    elif:
        imp_promedio(nom, ape, mat, lit, fis)

    print(nom +" "+ ape + " " + estado + destacado)

mi_nom=input("Ingrese el Nombre: ")
mi_ape=input("Ingrese el Apellido: ")
mi_mat=input("Ingrese la nota de matematica: ")
mi_lit=input("Ingrese la nota de literatura: ")
mi_fis=input("Ingrese la nota de fisica: ")

mi_promedio= imp_promedio(mi_nom, mi_ape, mi_mat, mi_lit, mi_fis)
#print(mi_promedio)
