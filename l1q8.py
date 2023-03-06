#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
#entrada
valor_hora_trabalho = float(input('Qual o valor da hora de trabalho: '))
quantidade_horas_trabalhas = int(input('Qual a quantidade de horas trabalhadas: '))

#processamento
salario_mensal = valor_hora_trabalho * quantidade_horas_trabalhas

#saída
print('O valor do salário mensal é: {}'.format(salario_mensal))