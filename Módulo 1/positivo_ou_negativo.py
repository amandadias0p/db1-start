# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

num = int(input("Digite um número: "))
if num > 0:
    print(f"O número {num} é positivo.")
elif num < 0:
    print(f"O número {num} é negativo.")
else:
    print(f"O número {num} é zero.")