#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#ºC = 5 * ((ºF-32) / 9).
#entrada
temperatura_fahrenheit = float(input('Temperatura em Fahrenheit: '))

#processamento
temperatura_celcius = 5 * (temperatura_fahrenheit - 32) / 9

#saída
print('A temperatura {:.1f}°F é igual a {:.1f}°C'.format(temperatura_fahrenheit, temperatura_celcius))
