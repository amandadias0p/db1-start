# Escreva uma classe em Python que leia dois números e implemente uma exponenciação

class Numeros:
    def __init__(self):
        pass

    def realizarPotencia(self, x, y):
        resultadoPotencia = x ** y
        return resultadoPotencia
    
resultado = Numeros()
base = int(input("Digite a base para a potenciação: "))
potencia = int(input("Digite a potência: "))

resultado = resultado.realizarPotencia(base, potencia)

print(f"O valor de {base} elevado a {potencia} é {resultado}")