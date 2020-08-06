#23. Leia um valor de comprimento em metros e apresente-o convertido em jardas.
#A fórmula de conversão é J = M/0.91, sendo M o valor em metros, e J o valor em jardas.

const= 0.91
metros = float(input('Digite um valor de comprimento em metros: '))
jardas = metros/const

print('O valor %.2f em metros, equivale à %.2f em jardas.' %(metros, jardas))
