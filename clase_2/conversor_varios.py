nota = """ 
Hola, este es un conversor de monedas a dolares
Ingresa a una de estas tres opciones:
1-soles a dolares
2-euros a dolares
3-pesos colombianos a dolares"""
print(nota)
opcion =int(input())
if opcion == 1:
    monto_soles =float(input('ingrese el monto en soles por vafor: '))
    tipo_de_cambio = 0.28
    monto_dolares = round(monto_soles* tipo_de_cambio,2)
    print(f'su monto en dolares es:{monto_dolares}')
elif opcion == 2:
    monto_euros =float(input('ingrese el monto en euros por vafor: '))
    tipo_de_cambio = 1.19
    monto_dolares = round(monto_euros* tipo_de_cambio,2)
    print(f'su monto en dolares es:{monto_dolares}')
else:
    monto_pesos_colombianos =float(input('ingrese el monto en pesos colombianos por vafor: '))
    tipo_de_cambio = 0.0027
    monto_dolares = round(monto_pesos_colombianos* tipo_de_cambio,2)
    print(f'su monto en dolares es:{monto_dolares}')

