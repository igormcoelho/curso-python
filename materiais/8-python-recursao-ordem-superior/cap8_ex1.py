def rsoma(lista, i=0):
    if i == len(lista):
        return 0
    else:
        return lista[i] + rsoma(lista, i + 1)
    
print(rsoma([1,2,3])) # 6

l=[1,2,3,4]
l2 = l[1:]
print(l2)
l2 += [1]
print(l)
print(l2)