#4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
#O número digitado ao quadrado;
#A raiz quadrada do número digitado.

from math import sqrt

numero = int(input('Digite um número inteiro qualquer: '))

if numero > 0:
    sqrt = sqrt(numero)
    quadrado = numero**2

    print(f'A raiz quadrada de {numero} é: {sqrt}.')
    print(f'O número {numero} ao quadrado é: {quadrado}.')
else:
  print('Número inválido.')
