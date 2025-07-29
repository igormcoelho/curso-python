x = 0

def fatorial(n):
   print('x:',x)
   f = 1
   i = 1
   while i<=n:
      f = f * i
      i = i + 1
   return f

a = 4
x = x + fatorial(a)
x = x + fatorial(7)
x = x + fatorial(5)

print(x) # 5184
