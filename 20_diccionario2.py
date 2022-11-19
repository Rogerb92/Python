print("--- "*5)
person= {
  'name': 'Camilo',
  'last_name': 'Rico',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name']='Roger Benitez'
person['age']-=69
person['langs'].append('java')
print(person)
del person['last_name']
person.pop('age')
print(person)


print(person.items())
print(person.keys())
print(person.values())
print(person.clear())

DATA2={
    "name": "Harry Potter",
    "species": "human",
    "gender": "male",
    "house": "Gryffindor",
    "dateOfBirth": "31-07-1980",
    "yearOfBirth": 1980,
    "ancestry": "half-blood",
    "eyeColour": "green",
    "hairColour": "black",
    "wand": {
      "wood": "holly",
      "core": "phoenix feather",
      "length": 11
    },
    "patronus": ["stag",'Fox'],
    "hogwartsStudent": True,
    "hogwartsStaff": False,
    "actor": "Daniel Radcliffe",
    "alive": True,
    "image": "https://hp-api.herokuapp.com/images/harry.jpg"
  }

print(DATA2)

#Agregando un dato a un diccionario que esta en un diccionario ppal
print(DATA2['wand']['core'])
DATA2['wand']['core']+= ' dragon heartstring'
print(DATA2['wand']['core'])

#agregando un valor a una lista que esta en un diccionario ppal
print(DATA2['patronus'])
DATA2["patronus"].append('cat')
print(DATA2['patronus'])

#eliminar un par clave, valor de una lista que esta en un diccionario ppal
del DATA2["actor"]
DATA2.pop('gender')
print(DATA2)

#Obtener items de un diccionario
print('')
print('Items')
print(DATA2.items())

#Imprime las keys del diccionario
print('')
print('keys')
print(DATA2.keys())


#imprime las keys del diccionar que esta en un diccionar ppal
print('')
print('keys of dict in dict')
print(DATA2["wand"].keys())

#Imprime los values  del diccionario
print('')
print('values')
print(DATA2.values())


#imprime las keys del diccionar que esta en un diccionar ppal
print('')
print('values of dict in dict')
print(DATA2["wand"].values())