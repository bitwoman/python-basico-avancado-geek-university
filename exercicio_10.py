#10.Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo).
#A fórmula de conversão é M = K/3.6, sendo K a velocidade em KM/h e M m/s.
km = float(input('Digite uma velocidade em km/h: '))
ms = km/3.6 

print('A velocidade %.2f em quilômetros por hora, equivale à %2.f em metros por segundo.' % (km,ms))
