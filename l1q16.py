"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a 
serem compradas e o preço total."""
import math
#entrada
area_pintada = float(input('Digite a área a ser pintada em matros quadrados: '))
#processamento
cobertura_da_tinta = area_pintada/3

numero_de_lata = cobertura_da_tinta/18

numero_de_lata_real = math.ceil(numero_de_lata)

valor_cada_lata = numero_de_lata_real * 80
#saída
print('Voce precisa de {:.0f}'.format(numero_de_lata_real))
print('Valor total: R${:.2f}'.format(valor_cada_lata))