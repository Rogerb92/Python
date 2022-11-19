# import de random
import random
# Definiendo las homologaciones
option = {'1' : 'Piedra','2' : 'Papel','3' : 'Tijera'}

victoriaUsuario=0
victoriaComputador=0
rondas=1
print('EL JUEGO DE PIEDRA, PAPEL O TIJERA. SE TERMINARA CUANDO ALGUIEN LLEGUE A 3 VICTORIAS.')

while True:

  print('*'*10)
  print('ROUND:',rondas)
  print('*'*10)

  # Petición de Datos a Usuario
  usuario = input('''PIEDRA PAPEL O TIJERA....Elige:
  
  1 para piedra
  2 para papel
  3 para tijera
  
  => ''')

  if not usuario in option:
    print('Debes ingresar solo los valores sugeridos.')
    continue
  
  #logica programa
  computador= str(random.randint(1,3))
  opcionEmp= usuario==computador
  opcionPer= (usuario=='1' and computador=='2') or (usuario=='2' and computador=='3') or (usuario=='3' and computador=='1')
  opcionGan= (computador=='1' and usuario=='2') or (computador=='2' and usuario=='3') or (computador=='3' and usuario=='1')
  
  
  
  #resultados
  print('Elegiste: ', option[usuario])
  print('El computador elige: ', option[computador])
  if opcionEmp:
    print("E S     U N   E M P A T E     E N     E L    R O U N D !")
  elif opcionPer:
    print("P E R D I S T E    E L    R O U N D !")
    victoriaComputador +=1
  elif opcionGan:
    print("G A N A S T E   E L    R O U N D !")
    victoriaUsuario +=1

  rondas +=1

  if victoriaComputador == 3:
    print("P E R D I S T E    E L    J U E G O!")
    break
  elif victoriaUsuario == 3:
    print("G A N A S T E   E L    J U E G O!")
    break