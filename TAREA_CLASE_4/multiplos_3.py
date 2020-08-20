def multiplos_3():
    contador = 0
    for i in range(int(input())):
        if i % 3 == 0:
            print(i)
            contador += 1
    print(f'hay {contador} numeros multiplos de 3')
multiplos_3()
