class Par:
    def __init__(self):
        self.x = 0
        self.y = 0

def desafio(muda_valores, a, par, lista):
    if muda_valores:
        par.x = -1
        lista += [-1]
        a += 1
    return

p1 = Par()
p1.x = 10
p1.y = 20

l1=[1,2,3]

z = 0

desafio(False, z, lista=l1, par=p1)
print(f'{p1.x} {p1.y} {z} {l1}')     # ???

desafio(True, z, lista=l1, par=p1)
print(f'{p1.x} {p1.y} {z} {l1}')     # ???
