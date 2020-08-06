#18. Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
#A fórmula de conversão é L = 1000 * M, sendo L o valor em litros e M o valor em metros cúbicos.

const = 1000
mc = float(input('Digite um valor em metros cúbicos: '))
litros = const * mc

print('O valor %.2f em metros cúbicos, equivale à %.2f em litros' %(mc, litros))
