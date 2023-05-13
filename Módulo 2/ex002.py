num = 10
for i in reversed(range(1, num // 2)): 
    if i % 2 == 0:
        print('* ' * num)
    else:
        print(' *' * num) 