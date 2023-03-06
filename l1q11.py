""" Faça um Programa que peça 2 números inteiros e um número real.
     Calcule e mostre:
 go produto do dobro do primeiro com metade do segundo.  
 a soma do triplo do primeiro com o terceiro.
 o terceiro elevado ao cubo."""

#entrada

numero_1 = int(input("Digite o 1o número inteiro: "))
numero_2 = int(input("Digite o 2o número inteiro: "))
numero_real = float(input("Digite um número real: "))

#processamento
calculo_1 = numero_1 * 2 * numero_2 / 2
calculo_2 = 3 * numero_1 + numero_real
calculo_3 = numero_real * numero_real * numero_real

#saída

print("o produto do dobro do primeiro com metade do segundo. {}").format(calculo_1)
print("a soma do triplo do primeiro com o terceiro. {}").format(calculo_2)
print("o terceiro elevado ao cubo. {}").format(calculo_3)