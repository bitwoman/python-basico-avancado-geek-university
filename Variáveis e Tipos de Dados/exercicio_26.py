#26. Leia um valor de área em metros quadrados e apresente-o convertido em hectares.
#A fórmula de conversão é H = M * 0.0001, sendo M como a área em metros quadrados e H em área de hectares.

const= 0.0001
metros_quadrados = float(input('Digite um valor de comprimento em metros quadrados: '))
hectares = metros_quadrados*const

print('O valor %.2f de comprimento em metros quadrados, equivale à %.4f de comprimento em hectares.' %(metros_quadrados, hectares))
