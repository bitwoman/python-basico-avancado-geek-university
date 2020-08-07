#47. Faça um programa que leia um inteiro positivo de quatro digítos (de 1000 à 9999) e imprima um número por linha.

numero = int(input('Digite um número: '))

if numero < 1000 or numero > 9999:
  numero = int(input('Digite um número: '))
else:
  numero = str(numero)
  
  for item in range(len(numero)):
    print(numero[item])
