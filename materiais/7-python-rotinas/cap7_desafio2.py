class ParInverte:
    def __init__(self):
        self.x = 0
        self.y = 0
    def inverte(self):
        aux = self.x
        self.x = self.y
        self.y = aux

def desafio2(par):
    par.inverte()

p1 = ParInverte()
p1.x = 10
p1.y = 20

print(f'{p1.x} {p1.y}')     # 10 20
desafio2(p1)
print(f'{p1.x} {p1.y}')     # ???
