def fatorial(n):
   f = 1
   i = 1
   while i<=n:
      f = f * i
      i = i + 1
   return f

def quebra_linha():
   print('')
   return

def linha(caracteres):
   i = 0
   while i <= caracteres:
      print('-', end='')
      i = i + 1
   quebra_linha()

print("imprimindo uma linha:")
linha(20)
fat5 = fatorial(5)
print(fat5)
