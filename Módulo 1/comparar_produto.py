# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

nomeProd1 = input("Informe o nome do 1º produto: ") 
valorProd1 = int(input("Informe o valor do 1º produto: "))
nomeProd2 = input("Informe o nome do 2º produto: ") 
valorProd2 = int(input("Informe o valor do 2º produto: "))
nomeProd3 = input("Informe o nome do 3º produto: ") 
valorProd3 = int(input("Informe o valor do 3º produto: "))

#descobrir o mais barato
if valorProd1 < valorProd2 and valorProd1 < valorProd3:
    menorValor = valorProd1
    menorNome = nomeProd1
elif valorProd2 < valorProd1 and valorProd2 < valorProd3:
    menorValor = valorProd2
    menorNome = nomeProd2
else:
    menorValor = valorProd3
    menorNome = nomeProd3

print(f"Você deve comprar o produto {menorNome}, pois ele é o mais barato, custando R$ {menorValor}.")