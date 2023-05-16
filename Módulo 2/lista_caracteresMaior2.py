# Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres sejam iguais

lista = ['abc', 'bdb', 'pk', 'banana', 'ukau', 'msuem', 'lq']
maior2 = 0
ultimo_primeiro = 0

for item in lista:
    if len(item) > 2:
        maior2 += 1
        if item[0] == item[-1]:
            ultimo_primeiro += 1
            print(f"O elemento {item} da lista possui mais que dois caracteres e o primeiro e último são iguais.")
        else:
            print(f"O elemento {item} da lista possui mais que dois caracteres.")
    else:
        print(f"O elemento {item} não se encaixa nos requisitos.")