#14. Leia um ângulo em graus e apresente-o convertido em radianos.
#A fórmula de conversão é R = G x PI/180, sendo G o ângulo em graus e R em radianos e PI = 3.14.

pi = 3.14
angulo_graus = float(input('Digite o valor de um ângulo em graus: '))
radianos = angulo_graus * pi/180

print('O ângulo %.2f em graus, equivale à %.2f em radianos.' %(angulo_graus, radianos))
