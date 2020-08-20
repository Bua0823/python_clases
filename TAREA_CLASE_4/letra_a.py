def frase():
    letras = 0
    for i in input('ingrese una frase porfa: '):
        if i == 'a':
            letras += 1
    print(f'se repite {letras} veces la letra "a" en la frase')
frase()
