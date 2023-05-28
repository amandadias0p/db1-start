# Escreva um programa que execute uma função que encontre o maior número de uma lista passada por parâmetro.
# Escreva um programa que execute uma função que some todos os itens de uma lista passada por parâmetro.
# Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro.


def encontrarMaiorNumero(lista): 
    maiorNumero = lista[0]
    for numero in lista:
        if numero > maiorNumero:
            maiorNumero = numero
    return maiorNumero

def somaLista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def multiplicaLista(lista):
    multiplicador = 1
    for numero in lista:
        multiplicador = multiplicador * numero
    return multiplicador

lista = []
resp = "s"

while resp == "s":
    resp = input("Deseja acrescentar algum número? [S/N] ").lower()
    
    while resp not in ["s", "n"]:
        print("Opção inválida. Digite 's' para adicionar um número ou 'n' para parar.")
        resp = input("Deseja acrescentar algum número? [S/N] ").lower()
    
    if resp == "n":
        break
    
    numeroLista = input("Digite um número para adicionar à lista: ")
    try:
        numeroLista = int(numeroLista)
        lista.append(numeroLista)
    except:
        print("O valor digitado não é valído. Tente com números inteiros.")
        continue

if not lista:
    print("A lista está vazia.")
else:
    maior = encontrarMaiorNumero(lista)
    soma = somaLista(lista)
    multiplicado = multiplicaLista(lista)
    print(f"O maior número da lista é {maior}")
    print(f"A soma dos números da lista é {soma}")
    print(f"A multiplicação dos valores da lista é {multiplicado}")