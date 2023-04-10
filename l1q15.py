"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    ◦ salário bruto.
    ◦ quanto pagou ao INSS.
    ◦ quanto pagou ao sindicato.
    ◦ o salário líquido.
    ◦ calcule os descontos e o salário líquido, conforme a tabela abaixo:
      + Salário Bruto : R$
      - IR (11%) : R$
      - INSS (8%) : R$
      - Sindicato ( 5%) : R$
      = Salário Liquido : R$
      Obs.: Salário Bruto - Descontos = Salário Líquido."""

#entrada
salario_hora = float(input('Digite quando voce ganha por hora: '))
hora_trabalho = float(input('Quantas horas voce trabalha? '))

#processamento
salario_bruto = salario_hora * hora_trabalho 

imposto_de_renda = salario_bruto - (11/100 * salario_bruto)

INSS = salario_bruto - (8/100 * salario_bruto)

sindicato = salario_bruto - (5/100 * salario_bruto)

salario_liquido = salario_bruto - ((11/100 * salario_bruto) + (8/100 * salario_bruto) + (5/100 * salario_bruto))

#saída
print('+ Salário Bruto: R${:.2f}'.format(salario_bruto))
print('- IR(11%): R${:.2f}'.format(imposto_de_renda))
print('- INSS(8%): R${:2f}'.format(INSS))
print('- Sindicato(5%): R${:.2f}'.format(sindicato))
print('= Salário liquido: R${:.2f}'.format(salario_liquido))