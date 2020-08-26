#17. Leia um valor de um comprimento em centímetros e apresente-o convertido em polegadas.
#A fórmula de conversão é P = C/2.54, sendo C o comprimento em centímetros, e P o comprimento em polegadas.

const = 2.54
centimetros = float(input('Digite um valor em centímetros: '))
polegadas = centimetros/const

print('O valor %.2f em centímetros, equivale à %.2f em polegadas' %(centimetros, polegadas))
