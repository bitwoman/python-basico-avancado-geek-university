#50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.

#O ano atual pode ser feita com importação de módulo, mas para ser de acordo com o nível da lista, o aconselhado é criar uma constante ou um input
# para que o usuário digite o ano atual também.
idade = int(input('Digite sua idade: '))
ano_atual = int(input('Digite o ano atual: '))
aniversario = str(input('Você já fez aniversário esse ano? ')).upper().strip()[0]

if aniversario == 'S':
  ano_nascimento = ano_atual - idade
else:
  if aniversario == 'N'
    ano_nascimento = (ano_atual - 1) - idade

print(f'O ano de nascimento do usuário é {ano_nascimento}')
