from sys import stdin

# [前,後,左,右,上,下]
# [4,3,5,2,1,6]

##list1_1 = [[4,3,5,2,1,6]] #一顆骰子
##list1_2 = [[4,3,5,2,1,6],[4,3,5,2,1,6]] #兩顆骰子
##
##list1 = list1_2

#輸入 list1,a,b 將list中的第 a,b 個骰子調換位置
def change(list1,a,b):
    pos_a = a-1
    pos_b = b-1
    list1[pos_a],list1[pos_b] = list1[pos_b],list1[pos_a]
    #print(list1)
    return list1
#change(list1_2,0,1)

#輸入 list1,a 將list中的第 a 個骰子向前旋轉
def turn_front(list1,a):
    pos_a = a-1
    temp = []
    temp.append(list1[pos_a][4]) #上變前
    temp.append(list1[pos_a][5]) #下變後
    temp.append(list1[pos_a][2]) #左不變
    temp.append(list1[pos_a][3]) #右不變
    temp.append(list1[pos_a][1]) #後變上
    temp.append(list1[pos_a][0]) #前變下
    list1[pos_a] = temp
    #print(list1)
    return list1
#turn_front(list1,1)

#輸入 list1,a 將list中的第 a 個骰子向右旋轉
def turn_right(list1,a):
    pos_a = a-1
    temp = []
    temp.append(list1[pos_a][0]) #前不變
    temp.append(list1[pos_a][1]) #後不變
    temp.append(list1[pos_a][5]) #下變左
    temp.append(list1[pos_a][4]) #上變右
    temp.append(list1[pos_a][2]) #左變上
    temp.append(list1[pos_a][3]) #右變下
    list1[pos_a] = temp
    #print(list1)
    return list1
#turn_right(list1,1)

n,m = map(int,stdin.readline().split())

list1 = []
for i in range(n):
    list1.append([4,3,5,2,1,6])

for i in range(m):
    a,b = map(int,stdin.readline().split())
    if a > 0 and b > 0:
        list1 = change(list1,a,b)
    elif b == -1:
        list1 = turn_front(list1,a)
    elif b == -2:
        list1 = turn_right(list1,a)

for i in range(n):
    if i == n-1:
        print(list1[i][4],end="")
    else:
        print(list1[i][4],end=" ")
