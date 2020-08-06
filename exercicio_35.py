#35. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = sqrt(a² + b²). Faça um programa que receba os valores de a e b 
#e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

from math import sqrt
a = int(input('Digite um valor para o cateto a: '))
b = int(input('Digite um valor para o cateto b: '))
hipotenusa = sqrt((a**2) + (b**2))

print('Hipotenusa: %.2f' %hipotenusa)
