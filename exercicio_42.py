#42. Receba o salário base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário base. 
#Além disso, ele paga 7% de imposto sobre o salário base.

salario_base = float(input('Digite o salário base de um funcionário: '))
com_gratificacao = salario_base + (salario_base * (5/100))
salario_sobre_imposto = com_gratificacao - (com_gratificacao * (7/100))

print(f'Salário base: {salario_base}\nSalário com gratificação de 5%: {com_gratificacao}\nSalário à ser recebido pelo funcionário com imposto de 7%: {salario_sobre_imposto}')
