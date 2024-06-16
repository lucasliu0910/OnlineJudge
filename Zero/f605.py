from sys import stdin

n,d = map(int,stdin.readline().split())
#print(n,d)

data = []
for i in range(n):
    data.append([int(a) for a in stdin.readline().split()])
#print(data)

##n_1,d_1 = 3, 4
##data_1 = [[24, 33, 42], [51, 48, 60], [77, 77, 77]]
##
##n_2,d_2 = 1, 3
##data_2 = [[24, 27, 21]]
##
##n,d,data = n_2,d_2,data_2

num = 0
cost = 0

for i in range(n):
    max_price = max(data[i])
    min_price = min(data[i])
    if abs(max_price - min_price) >= d:
        num += 1
        cost += (data[i][0]+data[i][1]+data[i][2])//3

print(num,cost)
