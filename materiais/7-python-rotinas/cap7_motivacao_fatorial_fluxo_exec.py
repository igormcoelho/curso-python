x=0

def fatorial(n):
   f = 1
   i = 1
   while i<=n:
      f = f * i
      i = i + 1
   return f

x = x + fatorial(4)
#                   -->
#                        def fatorial(n=4):
#                             computa fatorial f=1*2*3*4=24
#                             retorna f
#                   <--
# x = x   +   24
x = x + fatorial(7)
#                   -->
#                        def fatorial(n=7):
#                            ...
x = x + fatorial(5)
#                            ...
print(x) # 5184
