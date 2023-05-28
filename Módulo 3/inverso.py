# Escreva um programa que execute uma função que retorne o inverso de uma string passada por parâmetro

while True:
    texto = input("Digite uma palavra: ")
    if len(texto.split()) != 1:
        print("Digite apenas uma palavra!")
    elif not texto.isalpha():
        print("Digite apenas letras!")
    else:
        break


lista = list(texto)
lista.reverse()
listaInvertida = "".join(lista)
print(f"A palavra invertida é: {listaInvertida}")