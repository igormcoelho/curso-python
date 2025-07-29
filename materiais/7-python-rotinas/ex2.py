def busca1(chave, lista):
    i = 0
    while i < len(lista):
        if lista[i] == chave:
            return i
        i = i + 1
    return -1  # não encontrado

l1=[9,5,7]

print(busca1(5, l1)) # 1

def busca2(chave, lista):
    for (indice, valor) in enumerate(lista):
        if valor == chave:
            return indice
    return -1  # não encontrado

l1=[9,5,7]

print(busca2(5, l1)) # 1
