def desafio(muda_valores, a, lista):
    if muda_valores:
        a += 10
        lista += [a]
    return

l1=[1,2,3]

z = 5

desafio(False, z, l1)
print(f'{z} {l1}')     # ???

desafio(True, z, l1)
print(f'{z} {l1}')     # ???
