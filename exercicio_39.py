#39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:

#O primeiro ganhador receberá 46%;
#O segundo receberá 32%;
#O terceiro receberá o restante;
#Calcule e imprima a quantia ganha por cada um dos ganhadores.

premio = 780.000
premio_ganhador_1 = premio * (46/100)
premio_ganhador_2 = premio * (32/100)
premio_ganhador_3 = premio - premio_ganhador_1 - premio_ganhador_2 

print(f'Prêmio do ganhador 1º: {premio_ganhador_1}')
print(f'Prêmio do ganhador 2º: {premio_ganhador_2}')
print(f'Prêmio do ganhador 3º: {premio_ganhador_3}')
