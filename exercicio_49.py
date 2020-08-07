#49. Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração, em segundos, de uma experiência biológica. 
#O programa deve resultar com o novo horário (hora, minuto, segundo) do término da mesma.

#Início e duração em segundos.
inicio = int(input('Digite o horário em segundos do início da experiência: '))
duracao = int(input('Digite o horário em segundos da duração da experiência: '))
termino = duracao - inicio

horas = termino//3600
segundos = termino % 3600
minutos = segundos//60
segundos = segundos % 60

print(f'Horário do término é {horas}:{minutos}:{segundos}')
