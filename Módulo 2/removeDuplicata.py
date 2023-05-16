# Escreva um programa que remova itens duplicados de uma lista

lista_duplicada = [1, 2, 3, 3, 2, 6, 1, 13, 8, 11, 9, 7, 9, 7, 1, 0]
lista_nova = []

for item in lista_duplicada:
    if item not in lista_nova:
        lista_nova.append(item)

print(f"A lista antiga era: {lista_duplicada}. Após remover os itens duplicados, a lista ficará assim: {lista_nova}.")

# se a ordem não for importante, podemos transformar a lista em conjunto, pois o conjunto não permite itens duplicados

set_lista = set(lista_duplicada)
print(set_lista)

#podemos retransformar o conjunto em lista caso necessário

nova_lista = list(set_lista)
print(nova_lista)