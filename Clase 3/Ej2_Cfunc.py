#calcula el promedio
def promedio(mate, lite, fisi):
    prom =(mate + lite + fisi) /3
    return prom

#imprime los datos
def datos_del_alumno(nombre, apellido, prom):
    print ("El alumno " +nombre + " " +apellido+ " "+" tiene como promedio: " +str(prom) )

#Ver aprobacion del alumno
def estado_aprobacion(prom):
    if prom >=6:
        print("El alumno aprobo")
        if prom >9:
            print("Alumno destacado")
    elif prom >=4 and prom <6:
        print("A recuperatorio")
    else:
        print("Insuficiente")

nombre= input("Ingrese el nombre: ")
apellido= input("Ingrese el apellido: ")

a= True
while a==True:
    try:
        mate= int(input("Ingrese la nota de matematicas: "))
        while a== True:
            try:
                lite= int(input("Ingrese la nota de literatura: "))
                while a==True:
                    try:
                        fisi= int(input("Ingrese la nota de fisica: "))
                        a= False
                    except ValueError as e:
                        print('Debe ingresar un numero')
            except ValueError:
                print('Debe ingresar un numero')
    except ValueError:
        print('Debe ingresar un numero')

# while True:
#     try:
#         mate= int(input("Ingrese la nota de matematicas: "))
#
#         while True:
#             try:
#                 lite= int(input("Ingrese la nota de literatura: "))
#
#                 while True:
#                     try:
#                         fisi= int(input("Ingrese la nota de fisica: "))
#                         break;
#                         break;
#                         break;
#                     except ValueError as e:
#                         print('Debe ingresar un numero')
#             except ValueError:
#                 print('Debe ingresar un numero')
#     except ValueError:
#         print('Debe ingresar un numero')

promed=promedio(mate, lite, fisi)
datos_del_alumno(nombre, apellido, promed)
estado_aprobacion(promed)
