n = int(input())
scores = [int(i) for i in input().split()]

scores.sort()

print(*scores)

more = []

less = []

for i in scores:
  if i >= 60:
    more.append(i)
  else:
    less.append(i)

if len(less) == 0:
  print("best case")
else:
  print(max(less))

if len(more) == 0:
  print("worst case")
else:
  print(min(more))
