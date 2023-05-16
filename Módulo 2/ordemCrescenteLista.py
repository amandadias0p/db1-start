#Escreva um programa que ordene em ordem crescente uma lista de tuplas informadas, pelo último item da tupla (Exemplo de lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lista_tupla = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
num = 0

#opção 1
while num < (len(lista_tupla) - 1):
    if lista_tupla[num][-1] > lista_tupla[num+1][-1]:
        indice1 = lista_tupla[num]
        indice2 = lista_tupla[num+1]
        lista_tupla[num], lista_tupla[num+1] = indice2, indice1 #os itens de lugar
        num = 0
    else:
        num += 1

print(lista_tupla)

#opção 2
for i in range(len(lista_tupla) - 1):
    for j in range(len(lista_tupla) - 1 - i):
        if lista_tupla[j][-1] > lista_tupla[j + 1][-1]:
            lista_tupla[j], lista_tupla[j + 1] = lista_tupla[j + 1], lista_tupla[j] #troca os itens de lugar

print(lista_tupla)