# Escreva um programa que itere em um dicionário utilizando loops.
dicionario = {}

resp = "s"
while resp == "s":
    chave = input("Digite uma chave: ")
    valor = input("Digite um valor: ")
    dicionario[chave] = valor
    resp = input("Deseja continuar? [S/N] ").lower()

for chave in dicionario:
    print(f"A chave '{chave}' tem o valor '{dicionario[chave]}'")

