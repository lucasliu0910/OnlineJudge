def FIB(n):
  f0 = 0
  f1 = 1
  sum = 0
  for i in range(n):
    k = f1
    f1 = f0 + f1
    f0 = k
  return f1

n = int(input()) 
print(FIB(n))
