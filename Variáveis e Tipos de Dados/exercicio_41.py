#41. Faça um programa que leia o valor da hora de trabalho (em reais) e 
#número de horas trabalhadas no mês. Imprima o valor a ser pago para o funcionário, adicionando 10% sobre o valor calculado.

valor_hora_trabalhada = float(input('Digite o valor da hora de trabalho: '))
horas_trabalhadas_mes = int(input('Digite quantas horas foram trabalhadas: '))
valor_estimado = horas_trabalhadas_mes * valor_hora_trabalhada 
valor_calculado = valor_estimado + (valor_liquido * (10/100))

print(f'Valor calculado à ser pago: {valor_calculado}')
