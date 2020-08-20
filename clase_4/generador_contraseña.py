import random
def generador_contrasena():
    mayusculas = ['A', 'B', 'C','D','E','F','G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f','g']
    simbolos = ['!', '*', '#', '$', '%']
    numeros = ['1','2', '3','4','5','6','7']
    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    # print(contrasena)    
    contrasena = "".join(contrasena)
    return contrasena
# print(generador_contrasena())
# generador_contrasena()
nueva_contrasena = generador_contrasena()
print(f'tu contraseña es: {nueva_contrasena} ')
