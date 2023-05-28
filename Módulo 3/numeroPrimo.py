# Escreva um programa que execute uma função que receba um número informado no console como parâmetro e verifique se o número informado é primo ou não

def verificaNumeroPrimo(x):
    if x < 2:
        return False
    for num in range(2, x): #ele não vai até o x, vai até o número anterior
        if x % num == 0:
            return False #se encontrar algum número divisível entre o 2 e o x-1, retornará False
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

if numeroEhPrimo:
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")