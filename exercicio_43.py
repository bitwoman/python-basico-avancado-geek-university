#43. Escreva um programa de ajuda para vendedores. À partir de um valor total lido, mostre:

#o total a pagar com desconto de 10%;
#o valor de cada parcela, no parcelamento de 3x sem juros;
#a comissão do vendedor, no caso da venda ser à vista (5% sobre o valor com desconto);
#a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total);

valor = float(input('Digite o valor total de sua compra: '))
total_desconto = valor - (valor*(10/100))
valor_parcela_3 = valor/3
comissao_a_vista = total_desconto * (5/100) 
comissao_parcelada = valor * (5/100)

print(f'Total a pagar com desconto de 10%: {total_desconto}')
print('Valor de cada parcela (3x s/ juros): %.2f' %valor_parcela_3)
print(f'Comissão do vendedor de 5%, à vista sobre o valor com desconto: {comissao_a_vista}')
print(f'Comissão do vendedor de 5%, parcelada sobre o valor total: {comissao_parcelada}')
