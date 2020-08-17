ejemplo_2 = """Brenda se va de vacaciones y quiere 
comprar un regalo para todos sus pinkies,entonces
se dirige al mercado de chucherías pero el monto
de cada uno no debe pasar lo 200 soles entonces
crea un programa que le avise un mensaje de alerta.."""
costo_relago = [12, 46, 95, 346, 874, 26, 524, 245, 56, 57]
for i in costo_relago:
    if i >= 200:
        break
print(f'Alerta!!!! el monto {i} excende el presupuesto por regalo xd' )
    
