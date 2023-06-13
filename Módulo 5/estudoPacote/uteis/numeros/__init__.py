#criando o pacote

def fatorial(x):
    f = 1
    for cont in range(1, x+1):
        f *= cont
        
    return f

def dobro(x):
    d = x*2
    return d

def triplo(x):
    t = x*3
    return t