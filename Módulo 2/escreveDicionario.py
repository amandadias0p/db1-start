# Escreva um programa que leia chaves e valores, crie um dicionário, e depois, verifique se uma chave informada existe em um dicionário
resp2 = "s"
dicionario = {}

def escreve_dicionario():
    resp = "s"
    while resp == "s":
        chave = input("Digite uma chave: ")
        valor = input("Digite um valor: ")
        dicionario[chave] = valor
        resp = input("Deseja continuar? [S/N] ").lower()

escreve_dicionario()

perg = input("Gostaria de verificar a existência de alguma chave no dicionário? [S/N] ").lower()
if perg == "s":
    while resp2 == "s":
        verif = input("Qual chave deseja verificar? ")
        if verif in dicionario:
            print(f"A chave {verif} se encontra no dicionário. Seu valor é {dicionario[verif]}.")
        else:
            print(f"A chave {verif} não se encontra no dicionário.")
            adicionar = input("Deseja acrescentar? [S/N] ").lower()
            if adicionar == "s":
                escreve_dicionario()
        resp2 = input("Deseja continuar? [S/N] ").lower()

print(f"Finalizando. O dicionário digitado foi: {dicionario}")
