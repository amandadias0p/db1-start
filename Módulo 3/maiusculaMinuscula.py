# Escreva um programa que execute uma função que conte o número de letras maiúsculas e minúsculas de um texto e que ao final, chame outra função para imprimir o resultado

maiuscula = 0
minuscula = 0

def contaLetras(a):
    global maiuscula, minuscula
    for item in a:
        if a.isupper():
            maiuscula += 1
        else:
            minuscula += 1
    

def imprimeResultado():
    global maiuscula, minuscula
    print(f"A frase apresentada possui {maiuscula} caracteres maiúsculos e {minuscula} caracteres minúsculos.")

frase = input("Defina uma frase: ")
contaLetras(frase)
imprimeResultado()