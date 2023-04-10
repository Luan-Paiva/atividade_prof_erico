"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    ◦ Para homens: (72.7*h) - 58
    ◦ Para mulheres: (62.1*h) - 44.7"""

#entrada
altura = float(input('Digite sua altura: '))

#processamento
homens = (72.7*altura) - 58
mulheres = (62.1*altura) - 44.7

#saída
print('O peso ideal para homens é: {:.2f}'.format(homens))
print('O peso ideal para mulheres é: {:.2f}'.format(mulheres))