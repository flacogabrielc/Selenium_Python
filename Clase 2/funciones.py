#numero = input("Ingrese un numero: ")
#print(int(numero) + 20)

def ingresar_numero():
    numero = input("Ingrese un numero: ")
    numero = int(numero) + 20
    return numero

#mi_numero= ingresar_numero()
#print(mi_numero)

def hacer_algo_con_numeros(a, b):
    #a= 10
    #b= 10
    return a + b

roberto = 14
cacho = 16

mi_variable=hacer_algo_con_numeros(roberto, cacho)
print(mi_variable)
mi_variable=hacer_algo_con_numeros(9, 55)
print(mi_variable)
