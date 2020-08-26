#24. Leia um valor de área em metros quadrados m² e apresente-o convertido em acres.
#A fórmula de conversão é A = M * 0.000247, sendo M a área em metros e A a área em acres.

const= 0.000247
metros_quadrados = float(input('Digite um valor de comprimento em metros quadrados: '))
acres = metros_quadrados * const

print('O valor %.2f de comprimento em metros quadrados, equivale à %.6f de comprimento em acres.' %(metros_quadrados, acres))
