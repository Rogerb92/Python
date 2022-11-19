pet = str(input("Ingresa mascota: "));
if pet == "perro":
    print("Es un perro :3");
elif(pet == "gato"):
    print(f"Pense que tu mascota era un perro, pero me doy cuenta que es: {pet} lo que es mejor")
else:
    print("Lo sentimos no sabemos que mascota tienes")


stock = int(input("ingrese el stock: "))
if stock >= 100 and stock <= 1000:
  print("Gracias por sus preferir nuestros servicios, le enviaremos su pedido!")
else:
  print("Este stock es invalido, el stock debe ser un numero entre 100 y 1000")


print('Par o Impar')

number = int(input('Digita un número: '))

if (number % 2) == 0:
    print('Tu numero es par!')
else:
    print('Tu numero es Impar!')