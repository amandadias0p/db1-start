entrada1 = [(2, 4), (6, 3), (5, 10)]
entrada2 = [(4, 8), (16, 4)]
entrada3 = [(1, 2), (3, 6), (6, 12)]

saida1 = set() 
saida2 = set() 
saida3 = set()

for x, y in entrada1: 
    if x < y: 
        saida1.add(x) 
    else: 
        saida1.add(x // y)

for x, y in entrada2: 
    if x < y: 
        saida2.add(x) 
    else: 
        saida2.add(x // y)

for x, y in entrada3: 
    if x < y: 
        saida3.add(x) 
    else: 
        saida3.add(x // y)

print(f"Saida 1: {saida1}")
print(f"Saida 2: {saida2}")
print(f"Saida 3: {saida3}")