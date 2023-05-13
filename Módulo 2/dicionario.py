# Escreva um programa que conte o número de caracteres de uma string

string = input("Digite uma palavra para analisar: ")
dicionario  = {}

for letra in string:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

print(f"A quantidade de cada letra na palavra escolhida é: {dicionario}")