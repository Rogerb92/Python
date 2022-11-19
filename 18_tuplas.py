numeros = (1,4,5,6)
textos = ('Pablo','Isis','Erika')
print(numeros)
print('0-->',numeros[0])
print('-1-->',numeros[-1])
print(type(numeros))

print(textos)
print(type(textos))

#Las tuplas son inmutables

print(textos.index('Isis'))
print(textos.count('Erika'))

Lista = list(textos)
print(Lista)
print(type(Lista))

Lista[1]='Roger'
print(Lista)

tupla = tuple(Lista)
print(tupla)
print(type(tupla))
