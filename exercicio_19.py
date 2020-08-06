#19. Leia um valor de litros e apresente-o convertido em metros cúbicos m³.
#A fórmula de conversão é M = L/1000, sendo L o valor em litros e M o valor em metros cúbicos.

const = 1000
litros = float(input('Digite um valor em litros: '))
mc = litros/const

print('O valor %.2f em litros, equivale à %.2f em metros cúbicos.' %(litros, mc))
