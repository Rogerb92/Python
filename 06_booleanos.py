#valores booleanos, Tiene que se mayúscula la primera letra
Casado  = True
print("¿Estás casado ?", Casado)
print("")

#Problemas de infidelidad en la pareja, se separan
#Tiene que ser mayúscula en False
Casado = False
print("¿Estás casado ?", Casado)
print("")

#Reconciliación
inversion = not Casado
print(f"Reconcilación es {inversion}")
print("")

#Resumen
Amor = True
Infidelidad = False
print(f"La indifelidad hace que el amor se invierta, que el vínculo sea {not Amor}")
print("")
print(f"El perdón hace que el infidelidad se invierta, que el vínculo sea {not Infidelidad}")
print("")