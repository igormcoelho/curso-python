def maior(a,b):
   if a >= b:
      return a
   else:
      return b
    
print(maior(-5, 10)) # 10

def soma(lista):
   s = 0 
   for x in lista:
      s += x
   return s

print(soma([1,2,3])) # 6

print(max(-5, 10))   # 10

print(sum([1,2,3]))  # 6

print(max(1,2,3,4,5,6,7)) # 7

def maior_ilimitado(*parametros):
   if len(parametros) == 0:
      return -9999999
   m = parametros[0]
   i = 1
   while i < len(parametros):
      if parametros[i] > m:
         m = parametros[i]
      i = i + 1
   return m

print(maior_ilimitado())               # -9999999
print(maior_ilimitado(10))             # 10
print(maior_ilimitado(10, 0, 20, -5))  # 20

