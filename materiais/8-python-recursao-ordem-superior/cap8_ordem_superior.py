def rfatorial(n):
   if n == 0:
      return 1
   else:
      return n*rfatorial(n-1)
   
lista = []
lista.append(rfatorial)

print(lista)
# [<function rfatorial at 0x7ffaf27da340>]

print(lista[0](4)) # 24

def mapear(f, lista):
    resultado = []
    for x in lista:
        resultado.append(f(x))
    return resultado

def quadrado(x):
   return x*x

print(mapear(quadrado, [1,2,3]))
# [1, 4, 9]

print(mapear(lambda x: x * x, [1, 2, 3]))
# [1, 4, 9]
