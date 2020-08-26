#6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

numero_1 = int(input('Digite um número inteiro qualquer: '))
numero_2 = int(input('Digite um número inteiro qualquer: '))

if numero_1 > numero_2:
  diferenca = numero_1 - numero_2
  print(f'O número {numero_1} é o maior!')
  print(f'E a diferença entre eles é de: {diferenca}')
elif numero_2 > numero_1:
  diferenca = numero_2 - numero_1
  print(f'O número {numero_2} é o maior!')
  print(f'E a diferença entre eles é de: {diferenca}')
else:
  print('São iguais!')
