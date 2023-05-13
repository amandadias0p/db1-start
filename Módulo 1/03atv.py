# Um empresário da cidade promove anualmente uma campanha beneficente para arrecadar roupas para o inverno. Neste ano, para estimular as doações o empresário resolveu doar para às instituições beneficiadas R$ 2,00 por Kg de roupa doado pela população. Além disso, se o total de doações exceder a média das doações nos últimos 3 anos, haverá um bônus de R$ 3,00 para cada Kg de roupa que exceder a média. Desenvolva um algoritmo que receba do usuário o total de doações de cada um dos últimos 3 anos da campanha e o total de doações do ano atual e retorne como saída o total em R$ a ser doado para as instituições.  

media_doacoes = float(input("Informe a média de doações em KG dos últimos 3 anos: "))
doacoes_atual = float(input("Informe o total de doações em KG deste ano: "))
total = doacoes_atual * 2 #pega o total de doações do ano e multiplica por 2 para dar o valor a ser doado
excedente = doacoes_atual - media_doacoes #calcula o excedente ao tirar a media do valor de doações atual
if doacoes_atual > media_doacoes: #se a quantidade de doacoes atual for maior que a média das doações dos últimos 3 anos
    total += excedente * 3 #soma, no total a ser doado, 3 reais por kg excedente 
print(f"O total em doações será R$ {total:.2f}") 