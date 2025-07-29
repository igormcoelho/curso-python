x = 0
ultimo = 0

def fatorial(n):
   global ultimo
   f = 1
   i = 1
   while i<=n:
      f = f * i
      i = i + 1
   ultimo = f
   return f

a = 4
x = x + fatorial(a)
x = x + fatorial(7)
x = x + fatorial(5)

print(x)      # 5184
print(ultimo) # 5! = 120
