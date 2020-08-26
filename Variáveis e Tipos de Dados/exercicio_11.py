#11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora).
#A fórmula de conversão é K = M * 3.6, sendo K a velocidade em km/h, e M em m/s.

ms = float(input('Digite uma velocidade em m/s: '))
km = ms/3.6 

print('A velocidade %.2f em metros por segundo, equivale à %.2f em quilômetros por hora.' %(ms, km))
