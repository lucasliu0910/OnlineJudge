n,m = input().split()
n = int(n)
m = int(m)
num = []
# n,m = 3,2

num_pick = []

for i in range(n):
  num.append([int(i) for i in input().split()])
  num_pick.append(max(num[i]))
# num = [[3,2],[1,5],[6,4],[1,2]]
# num_pick = [5,6,1]

s = sum(num_pick)

print(s)

num_print = []

for i in num_pick:
  # print(f"i={i}")
  if s%i == 0:
    num_print.append(i)

# print(f"num_pick={num_pick}")
# print(f"num_print={num_print}")

if len(num_print) != 0:
  print(*num_print)
else:
  print(-1)
