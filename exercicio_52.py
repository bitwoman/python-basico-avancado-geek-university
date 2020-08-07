#52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. 
#Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

aposta_a1 = int(input('Digite o valor da sua contribuição para o prêmio: '))
aposta_a2 = int(input('Digite o valor da sua contribuição para o prêmio: '))
aposta_a3 = int(input('Digite o valor da sua contribuição para o prêmio: '))
premio = int(input('Digite o valor do prêmio: ')) 
premio_a1 = 0
premio_a2 = 0
premio_a3 = 0

#Amigo 1 = 1º 
#Amigo 2 = 2º
#Amigo 3 = 3º
if aposta_a1 > aposta_a2 and aposta_a1 > aposta_a3 and aposta_a2 > aposta_a3:
  premio_a1 = premio * (46/100)
  premio_a2 = premio * (32/100)
  premio_a3 = premio - premio_a1 - premio_a2
  print('Amigo 1: %.3f\nAmigo 2: %.3f\nAmigo 3: %.3f\n' %(premio_a1,premio_a2,premio_a3))
#Amigo 1 = 1º 
#Amigo 3 = 2º
#Amigo 2 = 3º
elif aposta_a1 > aposta_a2 and aposta_a1 > aposta_a3 and aposta_a3 > aposta_a2:
  premio_a1 = premio * (46/100)
  premio_a3 = premio * (32/100)
  premio_a2 = premio - premio_a1 - premio_a3
  print('Amigo 1: %.3f\nAmigo 2: %.3f\nAmigo 3: %.3f\n' %(premio_a1,premio_a2,premio_a3))
#Amigo 2 = 1º 
#Amigo 1 = 2º
#Amigo 3 = 3º
elif aposta_a2 > aposta_a1 and aposta_a2 > aposta_a3 and aposta_a1 > aposta_a3:
  premio_a2 = premio * (46/100)
  premio_a1 = premio * (32/100)
  premio_a3 = premio - premio_a1 - premio_a2
  print('Amigo 1: %.3f\nAmigo 2: %.3f\nAmigo 3: %.3f\n' %(premio_a1,premio_a2,premio_a3))
#Amigo 2 = 1º 
#Amigo 3 = 2º
#Amigo 1 = 3º    
elif aposta_a2 > aposta_a1 and aposta_a2 > aposta_a3 and aposta_a3 > aposta_a1:
  premio_a2 = premio * (46/100)
  premio_a3 = premio * (32/100)
  premio_a1 = premio - premio_a2 - premio_a3
  print('Amigo 1: %.3f\nAmigo 2: %.3f\nAmigo 3: %.3f\n' %(premio_a1,premio_a2,premio_a3))
#Amigo 3 = 1º 
#Amigo 1 = 2º
#Amigo 2 = 3º 
elif aposta_a3 > aposta_a1 and aposta_a3 > aposta_a2 and aposta_a1 > aposta_a2:
    premio_a3 = premio * (46/100)
    premio_a1 = premio * (32/100)
    premio_a2 = premio - premio_a1 - premio_a3
    print('Amigo 1: %.3f\nAmigo 2: %.3f\nAmigo 3: %.3f\n' %(premio_a1,premio_a2,premio_a3))
else:
#Amigo 3 = 1º 
#Amigo 1 = 2º
#Amigo 2 = 3º 
  if aposta_a3 > aposta_a1 and aposta_a3 > aposta_a2 and aposta_a2 > aposta_a1:
    premio_a3 = premio * (46/100)
    premio_a2 = premio * (32/100)
    premio_a1 = premio - premio_a3 - premio_a2
    print('Amigo 1: %.3f\nAmigo 2: %.3f\nAmigo 3: %.3f\n' %(premio_a1,premio_a2,premio_a3))    
