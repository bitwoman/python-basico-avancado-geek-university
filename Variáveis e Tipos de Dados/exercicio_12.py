#12. Leia uma distância em milhas e apresente-a convertida em quilômetros.
#A fórmula de conversão é K = 1.61 * M, onde K é a velocidade em km, e M é a distância em milhas.
m = float(input('Digite uma velocidade em milhas: '))
km = 1.61 * m 

print('A velocidade %.2f em milhas, equivale à %.2f em quilômetros por hora.' %(m, km))
