def es_la_marca(mar):
    if mar=='FORD':
        return True
    elif mar=='CHEVROLET':
        return True
    elif mar=='FIAT':
        return True
    else:
        return False

def son_las_puertas(puer):
    if puer=='2':
        return True
    elif puer=='4':
        return True
    elif puer=='5':
        return True
    else:
        return False

def es_color(col):
    if col=='BLANCO':
        return True
    elif col=='AZUL':
        return True
    elif col=='NEGRO':
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

def descuento(contador):
    if contador <=5:
        pdesc=1
    elif contador > 5 and contador < 11:
        pdesc=0.90
    elif contador > 10 < 51:
        pdesc=0.85
    else:
        pdesc=0.82
    return pdesc

respuesta =True
cont=0
comtot=0
precio=0
while respuesta==True:
    cont+=1
    precio=0
    nombre=input('Ingrese el nombre del comprador: ')
    apellido=input('Ingrese el apellido del comprador: ')
    marca=(input('Ingrese una marca: ')).upper()
    es_marca=es_la_marca(marca)
    while es_marca==False:
        marca=(input('Ingrese una marca: ')).upper()
        es_marca=es_la_marca(marca)

    if es_marca == True:
        puertas=input('Ingrese cantidad de puertas: ')
        son_puertas=son_las_puertas(puertas)

    while son_puertas==False:
        puertas=input('Ingrese cantidad de puertas: ')
        son_puertas=son_las_puertas(puertas)

    if son_puertas==True:
        color=(input('Ingrese el color: ')).upper()
        es_el_color=es_color(color)

    while es_el_color==False:
        color=(input('Ingrese el color: ')).upper()
        es_el_color=es_color(color)

    if es_el_color==True:
        precio= (calcular_precio(marca, puertas, color))
        comtot=comtot + precio
        des=descuento(cont)
        preciofin= des * comtot
        hayotro=(input('hay otro cliente para ingresar? si/no  ')).upper()

        if hayotro=='SI':
            es_marca==False
            #respuesta=True
        elif hayotro=='NO':
            print('La cantidad de ventas totales son: '  + str(cont) + ' ' + 'La venta total del dia es: $' + str(comtot) + '  ' + 'El precio total con descuento es: $' + str(preciofin))
            respuesta=False
