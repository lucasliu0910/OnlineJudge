r,c,m = map(int,input().split())

list1 = []

for i in range(r):
  list2 = [int(a) for a in input().split()]
  list1.append(list2)

move = [int(a) for a in input().split()]

# list1_1 = [[1, 1], [3, 1], [1, 2]]
# move_1 = [1, 0, 0]
# r_1,c_1,m_1 = 3,2,3

# list1_2 = [[3, 3], [2, 1], [1, 2]]
# move_2 = [0,1]
# r_2,c_2,m_2 = 3,2,2

# list1 = list1_2
# move = move_2
# r,c,m = r_2,c_2,m_2

def reverse(list_input): #旋轉0
  r = len(list_input)
  c = len(list_input[0])
  list_output = []
  for i in range(c-1,-1,-1):
    list_tmp = []
    for j in range(0,r):
      list_tmp.append(list_input[j][i])
    list_output.append(list_tmp)
  return list_output

def turn(list_input): #翻轉1
  r = len(list_input)
  list_output = []
  for i in range(r-1,-1,-1):
    list_output.append(list_input[i])
  return list_output

#reverse([[3, 6], [2, 5], [1,4]])

#print(list1)
#print(move)

for i in range(len(move)-1,-1,-1):
  k = move[i]
  #print(f"i={i},k={k}")
  if k == 0:
    list1 = reverse(list1)
    #print(f"list1={list1}")
  elif k == 1:
    list1 = turn(list1)
    #print(f"list1={list1}")

print(len(list1),len(list1[0]))

for i in range(len(list1)):
  print(*list1[i])
