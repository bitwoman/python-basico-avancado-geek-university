#15. Leia um ângulo em radianos e apresente-o convertido em graus.
#A fórmula de conversão é G = Rx180/PI, sendo G o ângulo em graus e R em radianos e PI = 3.14.

pi = 3.14
radianos = float(input('Digite o valor de um ângulo em radianos: '))
angulo_graus =  radianos * 180/pi

print('O ângulo %.2f em radianos, equivale à %.2f em graus.' %(radianos, angulo_graus))
