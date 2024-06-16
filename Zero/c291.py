n = int(input())
f = [int(i) for i in input().split()]

#n1 = 3
#n2 = 10
#f1 = [0,2,1]
#f2 = [4,7,2,9,6,0,8,1,5,3]

#n =  n1
#f = f1

idx = []
for i in range(n):
    idx.append(i)

count = 0

#找出idx最前面非-1的數 輸入為list: idx 輸出為 int
def search(idx):
    n = 0
    while idx[n] == -1:
        n += 1
    return idx[n]
#print(search([-1,-1,4,5,2]))
#print(search([1,-1,4,5,2]))


#紀錄現在的idx為final_num
#把idx的第idx個數改成-1，
#把list: f的第idx個設為新的idx並改成-1
#迴圈直到list: f的第idx數為final_num
#輸入為int, list:idx, list:f
def remove(idx_num,idx,f):
    global count
    count += 1
    final_num = idx_num
    while f[idx_num] != final_num:
        idx[idx_num] = -1
        a = f[idx_num]
        f[idx_num] = -1
        idx_num = a
    idx[idx_num] = -1
    f[idx_num] = -1
    return idx,f
    #print(f"idx={idx}")
    #print(f"f={f}")
    #print(f"idx_num={idx_num}")
#remove(0,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[4, 7, 2, 9, 6, 0, 8, 1, 5, 3])

#主程式
#直到sum(idx) == -1 * n 否則一直執行search(idx)
while sum(idx) != -1 * n:
    a = search(idx)
    idx,f = remove(a,idx,f)

#print(f"n={n}")
#print(f"idx={idx}")
#print(f"    f={f}")
#print(f"count={count}")
print(count)
