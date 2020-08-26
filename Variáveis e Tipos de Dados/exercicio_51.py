#51. Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância de origem (0,0).

#Importação da  função de raiz quadrada.
from math import sqrt 

x = int(input('Digite a coordenada x: '))
y = int(input('Digite a coordenada y: '))
r = sqrt((x**2) + (y**2))

print('Distância: %.2f' %r)
