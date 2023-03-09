# Faça um Programa que leia três números e mostre-os em ordem decrescente

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

#utilizando uma variável memoria para guardar o valor que estamos alterando
if num2 > num1:
    memoria = num1
    num1 = num2
    num2 = memoria
    if num2 > num3:
        memoria = num3
        num3 = num2
        num2 = num3
elif num3 > num2:
    memoria = num2
    num2 = num3
    num3 = memoria

print(f"A ordem decrescente dos números é: {num1}, {num2}, {num3}")