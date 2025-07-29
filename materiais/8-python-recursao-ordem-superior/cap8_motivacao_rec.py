def rfatorial(n):
   if n == 0:
      return 1
   else:
      return n*rfatorial(n-1)

print(rfatorial(4))         # 24

print(4*rfatorial(3))       # 24

print(4*3*rfatorial(2))     # 24

print(4*3*2*rfatorial(1))   # 24

print(4*3*2*1*rfatorial(0)) # 24

print(4*3*2*1*1) # 24
