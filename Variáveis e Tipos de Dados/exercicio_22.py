#22. Leia um valor de comprimento em jardas e apresente-o convertido em metros
#A fórmula de conversão é M = 0.91 * J, sendo M o valor em metros, e J o valor em jardas.

const= 0.91
jardas = float(input('Digite um valor de comprimento em jardas: '))
metros = const*jardas

print('O valor %.2f em jardas, equivale à %.2f em metros.' %(jardas, metros))
