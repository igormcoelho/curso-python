dados = [10, 20, 30]

print(dados.pop())      # 30
print(dados)            # [10, 20]

del dados[1]            # comando 'del' não retorna!
print(dados)            # [10]

dados.append(40)        # procedimento sem retorno
print(dados)            # [10, 40]

dados += [50, 51]       # operação '+=' não retorna!
print(dados)            # [10, 40, 50, 51]

dados.extend([60, 61])  # procedimento sem retorno
print(dados)            # [10, 40, 50, 51, 60, 61]
