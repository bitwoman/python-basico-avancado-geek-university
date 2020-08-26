#13. Leia uma distância em quilômetros e apresente-a convertida em milhas.
#A fórmula de conversão é M = K/1.61, sendo K a velocidade em quilômetros e M a distância em milhas.

km = float(input('Digite uma velocidade em quilômetros: '))
m =  km/1.61

print('A velocidade %.2f em quilômetros, equivale à %.2f em milhas.' %(km, m))
