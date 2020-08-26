#2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. 
#Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

from math import sqrt

numero = int(input('Digite um número inteiro qualquer: '))

if numero > 0:
    sqrt = sqrt(numero)
    print(f'A raiz quadrada de {numero} é: {sqrt}.')
else:
  print('O número é inválido.')
