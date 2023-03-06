import math
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#área do quadrado = l * l
#entrada
lado_do_quadrado = float(input('Digite o valor do lado do quadrado: '))

#processamento
area_do_quadrado = pow(lado_do_quadrado,2)

#resposta
print('O valor do quadrado da área é: {}'.format(area_do_quadrado * 2))