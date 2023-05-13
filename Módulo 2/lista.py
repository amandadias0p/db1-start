lista = []
while True:
    valor = int(input("Digite um valor para acrescentar na lista (somente números): "))
    lista.append(valor)

    opcao = input("Deseja acrescentar mais algum valor?[S/N] ").lower()
    if opcao != "s":
        break

print(f"Os valores na lista são {lista}")

#Escreva um programa que some todos os itens de uma lista
soma = sum(lista)
print(f"O resultado da soma dos valores da lista é {soma}.")

#Escreva um programa que multiplique todos os itens de uma lista.
mult = 1
for i in lista:
    mult *= i
print(f"O resultado da multiplicação dos valores da lista é {mult}.")

#Escreva um programa que retorne o maior e o menor número de uma lista
print(f"O maior valor da lista digitada é {max(lista)}, e o menor é {min(lista)}")