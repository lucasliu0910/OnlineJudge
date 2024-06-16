n = int(input())
#n = 5

list1 = []

for _ in range(n):
    list1.append([int(i) for i in input().split()])
##list1 = [[160, 180], [150, 200], [280, 300], [300, 330], [190, 210]]

list1.sort()
##print(list1)

list_merge = []

###找規律
##[[1,2],[4,8],[5,6],[7,9]]
##4 > 2, [[1,2,4,8],[5,6],[7,9]]
##5 < 8, 6<8, [[1,2,4,8],[7,9]]
##7 <8 but 9 > 8, [[1,2,4,9]]
##answer: 2-1 + 9-4 = 1 + 5 = 6

def merge(list_input): #操作list_merge與下一list合併；輸入為一維list；不用return
    a = list_input[0]
    b = list_input[1]
    if a > list_merge[len(list_merge)-1]:
        list_merge.append(a)
        list_merge.append(b)
    elif a <= list_merge[len(list_merge)-1] and b <= list_merge[len(list_merge)-1]:
        pass
    elif a <= list_merge[len(list_merge)-1] and b > list_merge[len(list_merge)-1]:
        list_merge[len(list_merge)-1] = b

for i in range(n):
    if i == 0:
        list_merge.append(list1[0][0])
        list_merge.append(list1[0][1])
    else:
        merge(list1[i])

#print(list_merge)

ans_sum = 0

for i in range(1,len(list_merge),2):
    ans_sum += list_merge[i]-list_merge[i-1]

print(ans_sum)
