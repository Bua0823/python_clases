def sum_par_impar():
    suma_pares = 0
    suma_impares = 0
    for i in range(101):
        print(i) 
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i
    print(f'la suma de los numeros pares es: {suma_pares} ')
    print(f'la suma de los numeros impares es {suma_impares} ')
sum_par_impar()