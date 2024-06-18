def insertion(n,data):
  for i in range(1,n):
    for j in range(i-1,-1,-1):
      if data[i] > data[j]:
        data.insert(j+1,data.pop(i))
        break
      if j == 0:
        data.insert(0,data.pop(i))
  return data

while True:
  n = int(input())
  ages = []
  if n == 0:
    break
  ages = [i for i in map(int,input().split())]
  ans = insertion(n,ages)
  print(*ans)
