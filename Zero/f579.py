from sys import stdin

##a_1,b_1 = 1,8
##n_1 = 5
##record_1 = [[1, 8, 0], [5, 6, 0], [2, 7, 0], [8, 1, 0], [33, 22, 0]]
##
##a_2,b_2 = 3,9
##n_2 = 2
##record_2 = [[3,12,9,-3,3,9,0], [17,3,25,3,-3,-3,9,0]]
##
##a,b = a_1,b_1
##n = n_1
##record = record_1

#將購物車更新成最終購買情況
def new(record):
    record_new = []
    for i in range(len(record)):
        temp = []
        for j in range(len(record[i])):
            if record[i][j] > 0:
                temp.append(record[i][j])
            elif record[i][j] < 0:
                #print(f"record[i][j]={record[i][j]}")
                #print("remove!")
                temp.remove(abs(record[i][j]))
            elif record[i][j] == 0:
                break
        record_new.append(temp)
    #print(record_new)
    return record_new
#record = new(record)

#輸入個人購物車狀況，檢查是否有A和B
def check(list1):
    output = True
    if a not in list1 or b not in list1:
        output = False
    return output
#print(check(record[0]))

a,b = map(int,stdin.readline().split())
#print(a,b)

n = int(stdin.readline())

record = []
for i in range(n):
    x = [int(k) for k in stdin.readline().split()]
    record.append(x)
#print(record)

record = new(record)

count = 0

for i in range(n):
    if check(record[i]) == True:
        count += 1

print(count)
