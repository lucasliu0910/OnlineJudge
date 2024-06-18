def selection(n,data):
  for i in range(n):
    mini = i
    for j in range(i,n):
      if data[j] < data[mini]:
        mini = j
    data[mini],data[i]=data[i],data[mini]
  return data

while True:
  n = int(input())
  ages = []
  if n == 0:
    break
  ages = [i for i in map(int,input().split())]
  ans = selection(n,ages)
  print(*ans)
