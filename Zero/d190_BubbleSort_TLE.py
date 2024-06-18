def bubble(n,data):
  for i in range(n):
    for j in range(n-1,i-1,-1):
      if data[j]<data[j-1]:
        data[j],data[j-1]=data[j-1],data[j]
  return data

while True:
  n = int(input())
  ages = []
  if n == 0:
    break
  ages = [i for i in map(int,input().split())]
  ans = bubble(n,ages)
  print(*ans)
