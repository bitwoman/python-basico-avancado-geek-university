#28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

numero_1 = int(input('Digite um primeiro valor: '))
numero_2 = int(input('Digite um segundo valor: '))
numero_3 = int(input('Digite um terceiro valor: '))

soma  = (numero_1**2) + (numero_2**2) + (numero_3**2)

print(f'A soma do quadrado dos três números equivale à {soma}.')
