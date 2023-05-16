# Escreva um programa que clone ou copie uma lista

lista = ['abc', 123, 'j2k', 'm4a', 825 ]
lista_copia = []

for item in lista:
    if item not in lista_copia:
        lista_copia.append(item)

print(f"A lista copiada foi: {lista_copia}")