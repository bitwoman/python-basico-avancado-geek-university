#48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundos = int(input('Digite um número: '))
horas = segundos//3600
segundos = segundos % 3600
minutos = segundos//60
segundos = segundos % 60

print(f'O numero: {numero} tem {horas} horas, {minutos} minutos e {segundos} segundos.')
