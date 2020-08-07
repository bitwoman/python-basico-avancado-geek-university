#53. Faça um programa para ler as dimensões de um terreno (comprimento c, e largura l), bem como o preço do metro da tela t. 
#Imprima o custo para cercar este mesmo terreno com tela.

comprimento = float(input('Digite o comprimento do terreno: ')) 
largura = float(input('Digite a largura do terreno: '))
preco_tela = float(input('Digite o valor do preço da tela: '))
area = comprimento * largura
custo_total = preco_tela * area

print(f'Custo total para a tela no terreno: R${custo_total}')
