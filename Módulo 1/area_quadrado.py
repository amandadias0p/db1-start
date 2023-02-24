# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Informe o lado do quadrado (em cm): "))
area = lado**2
dobro = area * 2
print("A area de um quadrado com os lados de", lado, "cm é de", area, "cm. O dobro desse valor é", dobro)