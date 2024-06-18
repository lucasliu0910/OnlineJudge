n = int(input())

s = 0

count = 0

for i in range(n):
  count += 1
  if count < n:
    if n%count == 0:
      #print(count)
      s += count

if s > n:
  print("Abundant Number")
elif s < n:
  print("Deficient Number")
else:
  print("Perfect Number")
