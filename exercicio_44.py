#44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. 
#Calcule e mostre quantos degraus o usuário deve subir para atingir seu objetivo.

altura_degrau_escada = int(input('Digite a altura de cada degrau da escada: '))
altura_escada = int(input('Digite a altura da escada: '))
altura_desejada = int(input('Digite a altura que deseja alcançar: '))

atingir_objetivo = altura_desejada/altura_degrau_escada

print(f'Faltam {atingir_objetivo} degraus para atingir o que deseja.')
