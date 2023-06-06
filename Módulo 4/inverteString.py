# Escreva uma classe em Python que possua 2 métodos, um chamado adicionar_string e outro chamado inverter_string. O primeiro método deverá receber uma string como parâmetro e armazená-la em um array. O segundo, deverá listar as strings invertidas no seu conteúdo e também, na sua ordem de inclusão.

class MinhaString:
    def __init__(self) -> None:
        self.strings = []

    def adicionar_string(self, novaString):
        self.strings.append(novaString)

    def inverter_tring(self):
        stringInvertidas = []
        for string in self.strings: 
            stringInvertida = string[::-1] #Inverte a string, forma reversa
            stringInvertidas.append(stringInvertida)
        return stringInvertidas
    
minhasStrings = MinhaString()
resp = "s"
while resp == "s":
    adicionaString = input("Digite uma string para adicionar: ")
    minhasStrings.adicionar_string(adicionaString)
    resp = input("Deseja continuar: [S/N] ").lower()
print(f"A lista de strings digitadas é {minhasStrings.strings}.")

finalStringInvertidas = minhasStrings.inverter_tring()

print(f"De forma invertida, ficam assim: {finalStringInvertidas}.")