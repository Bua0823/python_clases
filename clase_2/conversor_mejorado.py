nota = """ 
Hola, este es un conversor de monedas a dolares
Ingresa a una de estas tres opciones:
1-soles a dolares
2-euros a dolares
3-pesos colombianos a dolares"""
print(nota)
opcion =int(input())
# if opcion == 1:
#     monto =float(input('ingrese el monto por vafor: '))
#     tipo_de_cambio = 0.28
#     monto_dolares = round(monto * tipo_de_cambio,2)
#     print(f'su monto en dolares es:{monto_dolares}')
# elif opcion == 2:
#     monto =float(input('ingrese el monto por vafor: '))
#     tipo_de_cambio = 1.19
#     monto_dolares = round(monto * tipo_de_cambio,2)
#     print(f'su monto en dolares es:{monto_dolares}')
# else:
#     monto =float(input('ingrese el monto por vafor: '))
#     tipo_de_cambio = 0.0027
#     monto_dolares = round(monto * tipo_de_cambio,2)
#     print(f'su monto en dolares es:{monto_dolares}')

# def monto_dolares(opcion, tipo_de_cambio):
#     monto =float(input('ingrese el monto por vafor: '))
#     monto_dolares = round(monto * tipo_de_cambio,2)
#     print(f'su monto en dolares es:{monto_dolares}')
# if opcion == 1:
#     tipo_de_cambio = 0.28 
#     monto_dolares(opcion, tipo_de_cambio)
# elif opcion == 2:  
#     tipo_de_cambio = 1.19
#     monto_dolares(opcion, tipo_de_cambio)
# else:
#     tipo_de_cambio = 0.0027
#     monto_dolares(opcion, tipo_de_cambio)

    
def monto_dolares(moneda, tipo_de_cambio):
    monto =float(input(f'ingrese el monto en {moneda} por vafor: '))
    monto_dolares = round(monto * tipo_de_cambio,2)
    print(f'su monto en dolares es:{monto_dolares}')
if opcion == 1: 
    monto_dolares('soles', 0.28)
elif opcion == 2:  
    monto_dolares('euros', 1.19)
else:
    monto_dolares('pesos colombianos', 0.0027)