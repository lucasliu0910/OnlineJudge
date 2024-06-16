num = str(input())
# num = "131"

num = [int(i) for i in num]

list1 = []
list2 = []

for i in range(len(num)):
  # print(f"i={i}")
  if i%2 == 0: #若為偶數位
    list2.append(num[i])
  elif i%1 == 0 or i == 0: #若為奇數位
    list1.append(num[i])

# print(list1)
# print(list2)

answer = sum(list1) - sum(list2)

if answer < 0:
  answer = -answer

print(answer)
