
nombre = "Roger"
apellido = "Benitez"

print(nombre)
print(apellido)

nombreCompleto=nombre+" "+apellido

print(nombreCompleto)

print('Python es capaz de saber cuando inicio un string con la comilla doble o simple y es dinámico')

#formato
plantilla="Hola, mi nombre es "+nombre+" y mi apellido es "+apellido

print(plantilla)

plantilla2 = "Hola, mi nombre es {} y mi apellido es {}".format(nombre, apellido)

print(plantilla2)

plantilla3 = f"Hola, mi nombre es {nombre} y mi apellido es {apellido}"

print(plantilla3)