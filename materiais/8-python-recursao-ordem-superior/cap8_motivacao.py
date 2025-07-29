def fatorial(n):
   f = 1
   i = 1
   while i<=n:
      f = f * i
      i = i + 1
   return f

print(fatorial(4))         # 24

print(4*fatorial(3))       # 24

print(4*3*fatorial(2))     # 24

print(4*3*2*fatorial(1))   # 24

print(4*3*2*1*fatorial(0)) # ???