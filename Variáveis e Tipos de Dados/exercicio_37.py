#37.Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.

produto = float(input('Digite o preço do produto: '))
desconto = produto * (12/100)
novo_valor = produto - desconto

print('Valor com desconto: %.2f' %novo_valor)
