#Escreva um programa que concatene os dicionários abaixo e crie um novo

dicionario = {}
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}

dicionario.update(dic1)
dicionario.update(dic2)
dicionario.update(dic3)
print(f"O novo dicionário é: {dicionario}")