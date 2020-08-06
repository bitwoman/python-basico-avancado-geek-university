#34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do círculo é pi * raio², considere pi = 3.141592.

pi = 3.141592
raio = float(input('Digite o valor do raio: '))
area = pi * (raio**2)

print('A área do círculo é igual à %.2f' %area)
