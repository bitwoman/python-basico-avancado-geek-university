#8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
#A fórmula de conversão é C = K - 273.15, sendo C a temperatura em Celsius, e K a temperatura em Kelvin.
graus_kelvin = float(input('Digite o valor de uma temperatura em graus Kelvin: '))
graus_celsius = graus_kelvin - 273.15

print(f'A temperatura {graus_kelvin} em Kelvin, equivale à {graus_celsius} em Graus Celsius.')
