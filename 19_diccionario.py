# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

#Los diccionarios se compones de llave, valor.
# muy similares a un archivo .json
my_dict = {
    'avion': 'objeto volador',
    'name': 'Javier',
    'last_name': 'Sepulveda',
    'age': 109
}

print(my_dict)

#el tamaño del diccionario
print(len(my_dict))

#imprimiendo una llave 
print(my_dict['age'])

#La funcion get, si no existe el valor sale un mensaje none(Maneja el error)
# Se cambian los corchetes por parentesis(), ya que get es una funcion de python
print(my_dict.get('test'))

print(my_dict.get('last_name'))

print('name' in my_dict)
print('other' in my_dict)