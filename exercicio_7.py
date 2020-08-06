#7. Leia uma temperatura em Graus Fahrenheit e apresente-a convertida em Graus Celsius.
#A fórmula de conversão é C = 5.0 * (F - 32.0)/9.0, sendo C a temperatura em Celsius, e F a temperatura em Fahrenheit.
graus_fahrenheit = float(input('Digite o valor de uma temperatura em graus Fahrenheit: '))
graus_celsius = 5.0 * (graus_fahrenheit - 32.0)/9.0

print(f'A temperatura {graus_fahrenheit} em Fahrenheit, equivale à {graus_celsius} em Graus Celsius.')
