def rbusca(chave, lista, i=0):
    if i >= len(lista):
        return -1
    if lista[i] == chave:
        return i
    return rbusca(chave, lista, i+1)

l1=[1, 3, 10, 30, 31, 37, 100]

print(rbusca(31, l1)) # 4


def rbusca_bin(chave, lista, ini, fim):
    if ini > fim:
        return -1
    meio = (ini + fim) // 2
    if lista[meio] == chave:
        return meio
    elif chave < lista[meio]:
        return rbusca_bin(chave, lista, ini, meio - 1)
    else:
        return rbusca_bin(chave, lista, meio + 1, fim)
    
l1=[1, 3, 10, 30, 31, 37, 100]

print(rbusca_bin(31, l1, 0, len(l1)-1)) # 4
