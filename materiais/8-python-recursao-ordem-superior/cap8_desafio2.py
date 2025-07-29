def mapear(f, lista):
    resultado = []
    for x in lista:
        resultado.append(f(x))
    return resultado

texto = "10  30        50"
lista1 = texto.split()
print(lista1)
# ['10', '30', '50']

lista2 = mapear(int, lista1)
print(lista2)
# [10, 30, 50]
