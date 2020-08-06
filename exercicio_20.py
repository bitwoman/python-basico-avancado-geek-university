#20. Leia um valor de massa em quilogramas e apresente-o convertido em libras.
#A fórmula de conversão é L = K/0.45, sendo L o valor em libras e K o valor em quilogramas.

const = 0.45 
quilogramas = float(input('Digite um valor em quilogramas: '))
libras = quilogramas/const

print('O valor %.2f em quilogramas, equivale à %.2f em libras.' %(quilogramas, libras))
