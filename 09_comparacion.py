#Operadores de comparacion-----------------------------------
#son operadores de logica y regresan booleanos
'''
( > / < ) Mayor / Menor
( >= / <= ) Mayor o igual / Menor o igual
( == ) Igual
( != ) Diferente
'''
a = 10
b = 3
print(f"Estamos haciendo el ejercicio siempre teniendo como primera parametro {a} y como segundo parametro {b}")
print(f"igual: {a == b}") #compara si las variables son iguales
print(f"diferente: {a != b}") #compara si las variables son diferentes
print(f"mayor: {a > b}") #compara si la variable a es mayor que la variable b
print(f"menor: {a < b}") #compara si la variable a es menor que la variable b
print(f"mayor o igual: {a >= b}") #compara si la variable a es mayor o igual que la variable b
print(f"menor o igual: {a <= b}") #compara si la variable a es menor o igual que la variable b
print(f"and: {a > b and a == b}") #compara si las dos variables son verdaderas
print(f"or: {a > b or a != b}") #compara si una de las variables es verdadera