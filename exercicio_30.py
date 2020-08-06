#30. Leia um valor real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólar.

dolar = 5.29
real = float(input('Digite um valor em reais: '))
conversao = real/dolar

print('O valor de %.2f reais em dólar americano equivale à %.2f.' %(real, conversao))
