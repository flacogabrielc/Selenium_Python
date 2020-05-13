#2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
#3-Lo mismo con la cantidad de puertas y los colores.
#4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
#5-Si la cantidad de clientes fue:
#--5.1: 0 a 5 personas no hay descuento
#--5.2: 6 a 10 personas: hay un descuento del 10%
#--5.3: 11 a 50 personas: hay un descuento del 15%
#--5.4: Más de 50 personas: El descuento es del 18%
#6-Solo se va a mostrar que se vendió al final del programa
def es_la_marca(mar):
    if mar=='FORD':
        return True
    elif mar=='CHEVROLET':
        return True
    elif mar=='FIAT':
        return True
    else:
        return False

def calcular_precio(marc, puer, color):
    if marc=='FORD':
        pmarc=100000
    elif marc=='CHEVROLET':
        pmarc=120000
    elif marc=='FIAT':
        pmarc=78000

    if puer=='2':
        ppuer=50000
    elif puer=='4':
        ppuer=65000
    elif puer=='5':
        ppuer=70000

    if color=='BLANCO':
        pcolor=10000
    elif color=='AZUL':
        pcolor=20000
    elif color=='NEGRO':
        pcolor=30000

    pprecio= pmarc + ppuer + pcolor
    return pprecio

respuesta =True
while respuesta==True:
    precio=0
    nombre=input('Ingrese el nombre del comprador: ')
    apellido=input('Ingrese el apellido del comprador: ')
    marca=(input('Ingrese una marca: ')).upper()
    es_marca=es_la_marca(marca)
    if es_marca == True:
        puertas=input('Ingrese cantidad de puertas: ')
        color=(input('Ingrese el color: ')).upper()
        precio= (calcular_precio(marca, puertas, color))
        print('El nombre del comprador es: ' + nombre + ', el apellido del comprador es: ' + apellido + ' y el precio del auto es: ' + str(precio))
        hayotro=(input('hay otro cliente para ingresar? si/no  ')).upper()
        if hayotro=='SI':
            es_marca==False
            #respuesta=True
        elif hayotro=='NO':
            respuesta=False

#    else:
#        marca=(input('Ingrese una marca: ')).upper()
