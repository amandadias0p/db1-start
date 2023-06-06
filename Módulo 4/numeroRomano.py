# Escreva uma classe em Python para converter um número inteiro em um numeral romano

class ConversorRomano:
    def __init__(self):
        self.digitos_romanos = { #dicionário contendo os números romanos
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def converterParaRomano(self, numero):
        if numero <= 0:
            return "Valor inválido para converter em números romanos."

        numeralRomano = ''
        for valor, numeral in self.digitos_romanos.items():
            while numero >= valor: #enquanto o numero do parametro for maior que o valor do dicionário...
                numeralRomano += numeral #adiciona a string do número romano ao numeralRomano
                numero -= valor #subtrai o valor do número definido
                #loop vai para o próximo valor

        return numeralRomano

numeroConverter = ConversorRomano()
numero = int(input("Defina um número: "))
numeroRomano = numeroConverter.converterParaRomano(numero)

print(numeroRomano)
