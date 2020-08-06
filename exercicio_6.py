#6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
#A fórmula de conversão é F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
graus_celsius = float(input('Digite o valor de uma temperatura em graus Celsius: '))
graus_fahrenheit = graus_celsius * (9.0/5.0) + 32.0

print(f'A temperatura {graus_celsius} em Celsius, equivale à {graus_fahrenheit} em Graus Fahrenheit.')
