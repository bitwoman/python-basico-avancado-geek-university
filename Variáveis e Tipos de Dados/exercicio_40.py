#40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e 
#imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

dias_trabalhadores = int(input('Quais foram a quantidade de dias trabalhados: '))
valor_liquido = dias_trabalhadores * 30
pagamento = valor_liquido - (valor_liquido * (8/100))

print(f'Total à pagar para o encanador: {pagamento}')
