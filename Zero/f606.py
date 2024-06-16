from sys import stdin

n,m,k = map(int,stdin.readline().split())
##n_1,m_1,k_1 = 2,3,3
##n_2,m_2,k_2 = 1,3,3
##n,m,k = n_1,m_1,k_1

Q = []
for i in range(n):
    Q.append([int(a) for a in stdin.readline().split()])
##Q_1 = [[30, 23, 23],[5, 25, 3]]
##Q_2 = []
##Q = Q_1

#輸入各伺服器擺放位置(list)，輸出花費
#輸入[0] (伺服器數量必為1個)
def cost(pos):
    cost_sum = 0

    #加總每一位置到每一位置之流量
    
    Q_new = dict()
    for i in range(n):
        #print(f"i={i}")
        for j in range(m):
            #print(f"j={j}"):
            
            road = str(pos[i])+str("to")+str(j)
            #print(road)
            if road in Q_new:
                Q_new[road] += Q[i][j]
            else:
                Q_new[road] = Q[i][j]
            #print(Q_new)

    #加總每一路徑之能量
    #print(Q_new)
    
    for i in Q_new:
        #print(i)
        if len(i) == 4:
            a = i[0]
            b = i[3]
        elif len(i) == 6:
            a = i[0:2]
            b = i[4:6]
        elif len(i) == 5:
            if i[1:3] == "to":
                a = i[0]
                b = i[3:5]
            else:
                a = i[0:2]
                b = i[4]

        #print(f"a={a},b={b}")
        if a == b:
            cost_sum += Q_new[i]
        else:
            if Q_new[i] <= 1000:
                cost_sum += Q_new[i]*3
            else:
                cost_sum += 1000*3+(Q_new[i]-1000)*2
    #print(cost_sum)
    return cost_sum
#cost([0,0])

cost_all = []

for i in range(k):
    pos = [int(a) for a in stdin.readline().split()]
    cost_all.append(cost(pos))

#print(cost_all)
print(min(cost_all))
