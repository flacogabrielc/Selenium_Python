nombre= input("Ingrese el nombre: ")
apellido= input("Ingrese el apellido: ")
mate= int(input("Ingrese la nota de matematicas: "))
lite= int(input("Ingrese la nota de literatura: "))
fisi= int(input("Ingrese la nota de fisica: "))

prom= (mate + lite + fisi) /3

print ("El alumno " +nombre + " " +apellido+ " "+" tiene como promedio: " +str(prom) )

if prom >6:
    print("El alumno aprobo")
    if prom >9:
        print("Alumno destacado") 
elif prom >=4:
    print("A recuperatorio")
else:
    print("Insuficiente")
