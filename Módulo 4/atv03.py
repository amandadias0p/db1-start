#classe dada no enunciado do exercício. Comentários feitos por mim

class Car:
    def __init(self, marca: str, modelo: str, ano: int, consumo: float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.consumo = consumo #define o consumo de combustivel por km
        self.combustivel = 0
        self.kilometragem = 0

    def abastecer(self, qtde: float) -> bool:
        if self.__validar_tanque(qtde): #chama o método validar_tanque. se True, continua
            self.combustivel += qtde
            return True
        
        return False
    
    def percorrer_percurso(self, distancia: float):
        self.kilometragem += distancia
        self.__consumir_combustivel(distancia) #chama o método consumir_combustível

    def __validar_tanque(self, qtde: float):
        return self.combustivel + qtde > 50 #se for menor que 50, retorna False. se for maior, retorna True. Aqui acredito que o símbolo está trocado, pois não permite abastecer e deixar o carro com menos de 50 unidades
    
    def __consumir_combustivel(self, distancia: float):
        consumo = distancia/self.consumo #divide a distancia pelo consumo definido no objeto pra saber quanto ele consumiu
        self.combustivel -= consumo #reduz o consumo do combustível disponível

## A classe possui 6 atributos (marca, modelo, ano, consumo, combustivel e kilometragem), definidos no método construtor __init__. Possui dois métodos publicos (abastecer e percorrer_percurs) e dois métodos privados (__validar_tanque e __consumir_combustível)