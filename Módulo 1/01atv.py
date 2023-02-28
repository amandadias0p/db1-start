tempC = float(input("Informe a temperatura em ºC: "))
tempF = tempC * 1.8 + 32

print('A temperatura em F é: ' + str(tempF))
print(f'A temperatura em F é: {tempF:.1f}') 	
print('A temperatura em F é: {}'.format(tempF)) 	 
print(f'A temperatura em F é: {tempF:.f}') #forma errada
print(f'A temperatura em F é: {tempF}')  