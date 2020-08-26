#7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "números iguais".

numero_1 = int(input('Digite um número inteiro qualquer: '))
numero_2 = int(input('Digite um número inteiro qualquer: '))

if numero_1 > numero_2:
  print(f'O número {numero_1} é o maior!')
elif numero_2 > numero_1:
  print(f'O número {numero_2} é o maior!')
else:
  print('São iguais!')
