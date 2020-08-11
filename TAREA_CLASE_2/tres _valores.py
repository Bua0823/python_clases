a = float(input('hola, ingrese un numero:'))
b = float(input('ingrese el siguiente numero:'))
c = float(input('ingrese el siguiente numero:'))
if a == b or a == c or b == c :
    print('ALERTA!!!!! se ha introducido valores iguales ')
elif a > b > c:
    print(f'el numero {a} es el mayor y {c} es el menor: ')
elif a > c > b:
    print(f'el numero {a} es el mayor y {b} es el menor: ')
elif b > a > c:
    print(f'el numero {b} es el mayor y {c} es el menor: ')
elif b > c > a:
    print(f'el numero {b} es el mayor y {a} es el menor: ')
elif c > a > b:
    print(f'el numero {c} es el mayor y {b} es el menor: ')
elif c > b > a:
    print(f'el numero {c} es el mayor y {a} es el menor: ')


