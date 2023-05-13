tempViagem = int(input("Quantas horas de viagem? "))
velocidadeMedia = int(input("Qual a velocidade média do veículo (km/h)? "))
distancia = velocidadeMedia * tempViagem #para descobrir a distancia a ser percorida em km
consumo = distancia / 8 #consumo total de km/l
print(f"Serão necessários {consumo:.1f}L de combustível")
 
#resp: na linha 2, há um erro que impede o código de funcionar corretamente; devemos indicar que a resposta será int pois input só capta respostas em string