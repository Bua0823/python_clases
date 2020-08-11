# mensaje ="""
# hola
# como estas?
# elige una de estas opciones por favor
# 1
# 2
# 3
# 4"""
#print(mensaje)
opcion = int(input('ingrese una opcion: '))
#if opcion == 1:
    #print(f'la opcion que elegiste es {opcion}')
    #print('adios!')
#elif opcion == 2:
    #print(f'la opcion que elegiste es {opcion}')
    #print('adios!')
#elif opcion == 3:
    #print(f'la opcion que elegiste es {opcion}')
    #print('adios!')
#elif opcion == 4:
    #print(f'la opcion que elegiste es {opcion}')
    #print('adios!')
#else:
    #print('elegiste una opcion incorrecta xd :(')

# def mensaje(opcion):
#     print(f'la opcion que elegiste es {opcion}')
#     print('adios!')
# if opcion == 1:
#     mensaje(opcion)
# elif opcion == 2:
#     mensaje(opcion)
# elif opcion == 3:
#     mensaje(opcion)
# elif opcion == 4:
#     mensaje(opcion)
# else:
#     print('elegiste una opcion incorrecta xd :(')


# def mensaje(opcion):
#     print('hola!')
#     print('como estas?')
#     print(f'la opcion que elegiste es {opcion}')
#     print('adios!')
# if opcion == 1 or opcion == 2 or opcion == 3 or opcion ==4:
#     mensaje(opcion)
# else:
#      print('elegiste una opcion incorrecta xd :(')

def mensaje(opcion):
    mensajillo = f"""
    hola!
    como estas?
    la opcion que elegiste es {opcion}
    adios!"""
    print(mensajillo)    
if opcion == 1 or opcion == 2 or opcion == 3 or opcion ==4:
    mensaje(opcion)
else:
     print('elegiste una opcion incorrecta xd :(')