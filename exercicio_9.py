#9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
#A fórmula de conversão é K = C + 273.15, sendo C a temperatura em Celsius, e K a temperatura em Kelvin.
graus_celsius = float(input('Digite o valor de uma temperatura em graus Celsius: '))
graus_kelvin = graus_celsius + 273.15

print(f'A temperatura {graus_celsius} em Celsius, equivale à {graus_kelvin} em Graus Kelvin.')
