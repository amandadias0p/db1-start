#Escreva uma classe em Python para converter um número romano em um número inteiro.

class ConversorInteiro:
    def __init__(self):
        self.digitosInteiros = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I':1
        }

    def converterInteiro(self, numeralConverter):
        #if not numeralConverter.isalpha():
            #return "Numeral inválido."

        numeroAnterior = 0
        numeroInteiro = 0
        for caracter in reversed(numeralConverter): #percorre cada caractere no numeral (invertido)
            valor = self.digitosInteiros.get(caracter, 0) #procura o caractere no dicionário e retorna seu valor
            if valor >= numeroAnterior: #se o valor do caractere for maior ou igual ao valor do caractere anterior
                numeroInteiro += valor #somar
            else: #se for menor
                numeroInteiro -= valor #subtrair. ex: IV. Ao analisar o I, veremos que é menor que o V, e subtraimos
            valorAnterior = valor
        
        return numeroInteiro
    
    def extrairNumeralRomano(self, entrada): #validação para que seja extraído somente o numeral romano
        numeralRomano = ''
        caracteresValidos = 'IVXLCDM'

        for caracter in entrada: #passa cada caracter da entrada definida
            if caracter.upper() in caracteresValidos: #se o caracter está entre os caracteres válidos
                numeralRomano += caracter.upper() #escreve o numeral romano

        return numeralRomano

    
num = ConversorInteiro()
numeral = input("Digite um numeral romano: ")
numeral = num.extrairNumeralRomano(numeral) #o melhor seria fazer uma validação para verificar se o numeral romano é válido, tentar voltar no futuro e fazer isso
inteiro = num.converterInteiro(numeral)
print(f"O numeral romano {numeral} equivale ao inteiro {inteiro}.")


