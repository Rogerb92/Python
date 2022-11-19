text = "Ella sabe Python"
print(text[0])
print(text[1])

print(text[9]) ## Si le das una posicion que no existe, da error

size = len(text)

print('size ', size)# Como empieza en 0, no llega a la última

print(text[size - 1])

print(text[-1])

# Slicing
print(text[0:5]) # Obtener del índice 0 al índice 4 excluyendo el índice 5 

print(text[:10]) # Obtendrá siempre desde 0 si no se específica 

print(text[5:]) # Obtendrá siempre hasta el final de la cadena desde donde específicaste el inicio

print(text[10:16:2]) # Sí se agrega un salto, regresa del inicio al final por los saltos

print(text[::2]) # Inicio al final en saltos de 2