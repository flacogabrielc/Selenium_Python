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

for i in range(5):
    precio=0
    nombre=input('Ingrese el nombre del comprador: ')
    apellido=input('Ingrese el apellido del comprador: ')
    marca=(input('Ingrese una marca: ')).upper()
    puertas=input('Ingrese cantidad de puertas: ')
    color=(input('Ingrese el color: ')).upper()
    precio= (calcular_precio(marca, puertas, color))
    print('El nombre del comprador es: ' + nombre + ', el apellido del comprador es: ' + apellido + ' y el precio del auto es: ' + str(precio))
