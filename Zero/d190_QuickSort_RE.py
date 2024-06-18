def quickSort(in_list):
  L = []
  R = []
  if len(in_list) <= 1:
    return in_list
  pivot = in_list[0]
  #print(f"pivot={pivot}")
  for i in in_list[1:]:
    if i < pivot:
      L.append(i)
    elif i >= pivot:
      R.append(i)
  #print(f"L={L}")
  #print(f"R={R}")
  return quickSort(L)+[pivot]+quickSort(R)

while True:
  n = int(input())
  if n == 0:
    break
  ages = [i for i in map(int,input().split())]
  ans = quickSort(ages)
  print(*ans)
