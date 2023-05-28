# Escreva um programa que execute uma função que receba um número informado no console como parâmetro e verifique se o número informado é primo ou não

contDivisao = 0

def verificaNumeroPrimo(x):
    global contDivisao
    for num in range(1, x):
        if x % num == 0:
            contDivisao += 1
    if contDivisao > 2:
        return False
    else: 
        return True

            

while True:
    numero = input("Digite um número para verificar se é primo: ")
    if not numero.isnumeric():
        print("Digite um número!")
    elif " " in numero:
        print("Digite apenas um número!")
    else:
        numero = int(numero)
        break

numeroEhPrimo = verificaNumeroPrimo(numero)
print("Verificando...")

print(f"O número {numero} foi divisível por {contDivisao} número(s), além dele mesmo.")
if numeroEhPrimo:
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")