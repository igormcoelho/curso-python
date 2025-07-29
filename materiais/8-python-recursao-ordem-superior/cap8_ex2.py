def filtrar(f, lista):
    nova = []
    for x in lista:
        if f(x):
            nova += [x]
    return nova

l1 = [1, 2, 3, 4, 5, 6]
l2 = filtrar(lambda x: x % 2 == 0, l1)
print(l2)

