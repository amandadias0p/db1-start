# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

dmt = float(input("Informe o diâmetro do círculo: "))
raio = dmt / 2
area = round((3.14159265359 * (raio ** 2)), 2)
print("A área de um círculo com diâmetro", dmt, "é ígual a:", area)