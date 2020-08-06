#38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.

salario = float(input('Digite o valor do salário antigo: '))
aumento = salario * (25/100)
novo_valor = salario + aumento

print('Novo salário: %.2f' %novo_valor)
