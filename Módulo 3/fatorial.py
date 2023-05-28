def fatorial(x):
    fat = 1
    print("Calculando...")
    for num in range (1, x+1):
        fat *= num
        print(f"Multiplicando por {num}. Resultado: {fat}")
    return fat

while True:
    numero = input("Digite um número: ")
    if not numero.isnumeric():
        print("Digite um número!")
    elif " " in numero:
        print("Digite apenas um número!")
    else:
        numero = int(numero)
        break

numeroFatorial = fatorial(numero)

print(f"O resultado do fatorial de {numero} é {numeroFatorial}.")