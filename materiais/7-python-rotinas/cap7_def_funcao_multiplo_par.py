class Par:
    def __init__(self):
        self.x = 0
        self.y = 0

def soma_multiplica(par):
    p2 = Par()
    p2.x = par.x+par.y
    p2.y = par.x*par.y
    return p2

p1 = Par()
p1.x = 10
p1.y = 20

p2 = soma_multiplica(p1)

print(f'{p1.x} {p1.y}')  # 10 20
print(f'{p2.x} {p2.y}')  # 30 200