#Faça um programa que peça as 4 notas bimestrais e mostre a média.
soma = 0
for valor in range(1,5):
    nota = float(input(f"Digite o valor da {valor}ª nota: "))
    soma += nota
media = soma/4
print(f"A média dos 4 bimestres é: {media:.1f}")