#Uma loja de departamentos possui dois tipos de vendedor: Vendedor Comum e Vendedor Comissionado. O vendedor comum possui um salário fixo, que varia de acordo com o setor da loja em que atua. Já para o vendedor comissionado, além do salário fixo, recebe uma comissão de 10% sobre o total de vendas no mês. Desenvolva uma hierarquia de classes que permita a implementação deste cenário. Função dada pelo enunciado do exercício. Comentários feitos por mim.

from enum import Enum

class Setor(Enum): #define o setor e sua enumeração (valor)
    ELETRODOMESTICOS = 'ELETRODOMESTICOS'
    ELETRONICOS = 'ELETRONICOS'
    VESTUARIO = 'VESTUARIO'

class Vendedor:
    __salarios = { #define os salários de acordo com o setor. variável privada __
    Setor.ELETRODOMESTICOS: 5000,
    Setor.ELETRONICOS: 7000,
    Setor.VESTUARIO: 4000,
}

    def __init__(self, nome: str, setor: Setor): #o setor só pode ser um valor dentro da classe Setor
        self.nome = nome #parâmetro comum
        self.setor = setor #parâmetro comum

    def obter_salario(self) -> float:
        return self.__salarios[self.setor] #retorna o salario de acordo com o setor

class VendedorComissionado(Vendedor): #recebe os atributos e classes de Vendedor
    def __init__(self, nome: str, setor: Setor):
        super().__init__(nome, setor) #chama os atributos da classe Pai
        self.__vendas = 0 #atributo de instância, permite que cada objeto tenha seu próprio valor para o atributo vendas. não é necessário definir esse valor ao criar um objeto, podemos atribuir e modificar o valor depois. privado

    def registrar_venda(self, valor: float): #modifica o atributo __vendas
        self.__vendas += valor

    def obter_salario(self) -> float:
        salario_base = super().obter_salario() #obtem o método da classe Pai. a classe Filha possui acesso ao método, e não a variavel privada __salarios
        return salario_base + self.obter_comissao() #acrescenta comissão no salário
    
    def obter_comissao(self) -> float:
        return self.__vendas * 0.05 #não deveria ser 0.10??
    
def exibir_salario(vendedor: Vendedor): #recebe o atributo vendedor que deve estar na classe Vendedor. classe VendedorComissionado está dentro de Vendedor
    print(f"O salário de {vendedor.nome} é {vendedor.obter_salario()}") #obtém o salario do vendedor com a função da classe Vendedor

vendedor_a = Vendedor('Vendedor A', Setor.VESTUARIO) #define nome e setor do vendedor A

vendedor_b = VendedorComissionado('Vendedor B', Setor.ELETRODOMESTICOS) #define nome e setor do vendedor comissionado B. lembrando que ele recebe uma comissão de 5% pela função. O enunciado diz ser 10, mas forneceu um código com 5%

vendedor_b.registrar_venda(25000) #registrando venda de 25.000 para o vendedor B
 
exibir_salario(vendedor_a) 
exibir_salario(vendedor_b) 