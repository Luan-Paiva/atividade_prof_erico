#Tendo como dados de entrada a altura de uma pessoa, construa um algoritimo que calcule seu peso ideal, usando a seguinte fórmula: 
# °(72.7*altura) - 58

#entrada
altura = float(input('Digite sua altura: '))

#processamneto
peso_ideal = 72.7 * altura - 58

#saída
print('O seu peso ideal é {:.2f}'.format(peso_ideal))