##field_1 = [[10,2,-1],[5,-1,2]]
##r_1,c_1,k_1,m_1 = 2,3,4,1
##
##field_2 = [[24, 52, 13, -1], [-1, 98, 8, -1]]
##r_2,c_2,k_2,m_2 = 2,4,6,2
##
##field = field_1
##r,c,k,m = r_1,c_1,k_1,m_1

#輸入(i,j)檢查該格鄰近多少個城市，-1不非城市不計入
def check(i,j):
    count = 0
    try:
        if field[i-1][j] != -1 and (i-1) >= 0: #檢查上
            #print(f"field[i-1][j]={field[i-1][j]}")
            count += 1
    except:
        pass
    try:
        if field[i+1][j] != -1: #檢查下
            #print(f"field[i+1][j]={field[i+1][j]}")
            count += 1
    except:
        pass
    try:
        if field[i][j-1] != -1 and (j-1) >= 0: #檢查左
            #print(f"field[i][j-1]={field[i][j-1]}")
            count += 1
    except:
        pass
    try:
        if field[i][j+1] != -1: #檢查右
            #print(f"field[i][j+1]={field[i][j+1]}")
            count += 1
    except:
        pass
    #print(f"count={count}")
    return count
#check(1,1)

#計算field每格每天移出量，存成list
def out():
    out_list = []
    for i in range(0,r):
        x = []
        for j in range(0,c):
            if field[i][j] != -1:
                count = check(i,j)
                x.append((field[i][j]//k)*count)
            else:
                x.append(0)
        out_list.append(x)
    #print(out_list)
    return out_list
#out()

#計算field每格每天移入量，存成list
def enter():
    enter_list = []
    for i in range(0,r):
        x = []
        for j in range(0,c):
            count = 0 #每個的移入量總和
            if field[i][j] != -1:
                try:
                    if field[i-1][j] != -1 and (i-1) >= 0: #檢查上
                        #print(f"field[i-1][j]={field[i-1][j]}")
                        count += field[i-1][j]//k
                except:
                    pass
                try:
                    if field[i+1][j] != -1: #檢查下
                        #print(f"field[i+1][j]={field[i+1][j]}")
                        count += field[i+1][j]//k
                except:
                    pass
                try:
                    if field[i][j-1] != -1 and (j-1) >= 0: #檢查左
                        #print(f"field[i][j-1]={field[i][j-1]}")
                        count += field[i][j-1]//k
                except:
                    pass
                try:
                    if field[i][j+1] != -1: #檢查右
                        #print(f"field[i][j+1]={field[i][j+1]}")
                        count += field[i][j+1]//k
                except:
                   pass
                x.append(count)
            else:
                x.append(0)
        enter_list.append(x)
    #print(enter_list)
    return enter_list
#enter()

#計算一天過後每格移出量和移入量之和
def main():
    sum_list = []
    out_list = out()
    enter_list = enter()
    for i in range(0,r):
        x = []
        for j in range(0,c):
            x.append(field[i][j]-out_list[i][j]+enter_list[i][j])
        sum_list.append(x)
    #print(sum_list)
    return sum_list
#main()

r,c,k,m = map(int,input().split())

field = []
for i in range(r):
    field.append([int(a) for a in input().split()])
#print(field)

for i in range(m):
    field = main()

population = []
#將field裡的人數展開成一維list
for i in range(0,r):
    for j in range(0,c):
        if field[i][j] != -1:
            population.append(field[i][j])
        else:
            pass

print(min(population))
print(max(population))
