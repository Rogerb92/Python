texto = 'hola Gabriel. hoy vi a jUAn Y a elvira'
mayusculas = []
for i in texto:
  if i.isupper():
    mayusculas.append(i)
print (mayusculas)


for element in range(1,21):
  print(element)

lista = [123,12,134,162,1455,134,11]

for elementos in lista:
  print(elementos)

tupla = ('Eri','Pablin','Isis','Roger','Benitez')

for elementos in tupla:
  print(elementos)

diccionario = {
  'nombre':'Eri',
  'mascota1':'Pablin',
  'mascota2':'Isis',
  'husbandName':'Roger',
  'husbandLastName':'Benitez'}

for elementos in diccionario:
  print(elementos, '-->', diccionario[elementos] )

for elementos,valor in diccionario.items():
  print(elementos, '-->', valor )

personas = [
  {
    'nombre':'Eri',
    'mascota':'Pablin'
  },
  {
    'nombre':'Roger',
    'mascota':'Isis' 
  },
  {
    'nombre':'Adri',
    'mascota':'Pichi' 
  }
]

for persona in personas:
  print(persona )