#3. Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao contrário.

from math import sqrt

numero = int(input('Digite um número inteiro qualquer: '))

if numero > 0:
    sqrt = sqrt(numero)
    print(f'A raiz quadrada de {numero} é: {sqrt}.')
else:
    quadrado = numero**2
    print(f'O número {numero} ao quadrado é: -{quadrado}.')
