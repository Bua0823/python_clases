velocidad_km_h = float(input('hola, ingrese la velocidad en km/h:'))
def velocidad_cm_s(velocidad_km_h):
    velocidad_cm_s = round (velocidad_km_h * 1000 * 100 / 3600, 0)
    print (f'la velocidad en cm/s es: {velocidad_cm_s}')
velocidad_cm_s(velocidad_km_h)  

