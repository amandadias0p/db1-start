soma = 0
cont = 0
for valor in range(1,5):
    num = int(input(f"Digite o {valor}º número: "))
    if num%2==0:
        cont += 1
        soma += num
print(f"Você digitou {cont} números pares, e a soma deles é: {soma}.")