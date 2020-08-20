def numeros_impares():
    contador = 0
    for i in range(101):
        if i % 2 != 0:
            contador += 1
            print(i)
    print(f'el numero de impares es: {contador} ' )
numeros_impares()