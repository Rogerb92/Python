# AND y
print('AND')
print('True and True =>', True and True) # True
print('True and False =>', True and False) # False
print('False and True =>', False and True) # False
print('False and False =>', False and False) # False

print(10 > 5 and 5 < 10) # True
print(10 > 5 and 5 > 10) # False


stock = input('Ingrese el numero de stock ')
stock = int(stock)

print("Hay inventario disponible?: ", stock >= 100 and stock <= 1000)

# OR o
print('OR')
print('True or True =>', True or True) # True
print('True or False =>', True or False) # True
print('False or True =>', False or True) # True
print('False or False =>', False or False) # False

role = input('Digita el rol => ')
print("Solo es True si eres vendedor o administrador: ", role == 'admin' or role == 'seller') # Es administrado o vendedor