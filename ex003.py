achou = False 
i = 0
frase="Aprendendo a programar"
while (not achou) and (i < len(frase)): 
    print(i)
    if i % 2 == 0: 
        i += 1
        continue 
    if frase[i] == ' ': 
        achou = True 
    i += 1 