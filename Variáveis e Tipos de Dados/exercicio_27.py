#27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
#A fórmula de conversão é M = H * 10000, sendo M como a área em metros quadrados e H em área de hectares.

const= 10000
hectares = float(input('Digite um valor de comprimento em hectares: '))
metros_quadrados = hectares*const

print('O valor %.2f de comprimento em hectares, equivale à %.2f de comprimento em metros quadrados.' %(hectares, metros_quadrados))
