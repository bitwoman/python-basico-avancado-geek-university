#25. Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
#A fórmula de conversão é M = A * 4048.58, sendo M a área em metros e A a área em acres.

const= 4048.58
acres = float(input('Digite um valor de comprimento em acres: '))
metros_quadrados = acres * const

print('O valor %.2f de comprimento em acres, equivale à %.2f de comprimento em metros quadrados.' %(acres, metros_quadrados))
