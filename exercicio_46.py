#46. Faça um programa que leia um inteiro positivo de três digítos (de 100 à 999). 
#Gere outro número formado pelos digítos invertidos do número lido. Exemplo: numero_lido = 123, numero_gerado = 321

#Dá pra usar lista e função nativa também, mas não englobava nesta sessão de tipos de dados.

numero = int(input('Digite um número: '))

if numero < 100 or numero > 999:
  numero = int(input('Digite um número: '))
else:
  numero = str(numero)
  
  for item in range(len(numero) - 1, -1, -1):
    print(numero[item], end='') #end sem espaçamento é para o resultado aparecer na mesma linha.
