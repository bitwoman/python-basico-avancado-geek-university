#16. Leia um valor de um comprimento em polegadas e apresente-o convertido em centímetros.
#A fórmula de conversão é C = P x 2.54, sendo C o comprimento em centímetros, e P o comprimento em polegadas.

const = 2.54
polegadas = float(input('Digite um valor em polegadas: '))
centimetros = polegadas * const

print('O valor %.2f em polegadas, equivale à %.2f em centímetros' %(polegadas, centimetros))
