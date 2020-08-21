contador = 0
def lista():
    mayusculas = ['A', 'B', 'C','D','E','F','G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f','g']
    simbolos = ['!', '*', '#', '$', '%']
    numeros = ['9','2', '3','4','5','6','1']
    lista = mayusculas + minusculas + simbolos + numeros
    lista_caracteres = []
    for i in lista:
        lista_caracteres.append(i)
        contador += 1
        if contador >= 2 and contador <= 100:
        else:
            print('cadena invalida')
    print(lista_caracteres)
lista()

