longitud = float(input('ingrese la longitud del poligono: '))
ancho = float(input('ingrese el ancho del poligono: '))
if longitud == ancho:
    area = longitud ** 2
    print(f'es un cuadrado cuya area es: {area} ')
else:
    perimetro = 2 * (longitud + ancho)
    print(f'es un rectangulo cuyo perimetro es: {perimetro} ')
    