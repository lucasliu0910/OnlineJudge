from sys import stdin

m_1,n_1 = 3,7
m_2,n_2 = 2,7

list1_1 = [1,2,3,5,4,5,4]
list1_2 = [1,2,2,1,2,1,2]

m,n = map(int,stdin.readline().split())
#m,n = m_1,n_1

list1 = [int(x) for x in stdin.readline().split()]
#list1 = list1_1

count = 0

dict1 = dict()

for i in range(0,n):
    if i >= m:
        dict1[list1[i-m]] -= 1
        if dict1[list1[i-m]] == 0:
            dict1.pop(list1[i-m])
    if list1[i] not in dict1:
        dict1[list1[i]] = 1
    else:
        dict1[list1[i]] += 1
    #print(f"dict1={dict1}")
    if len(dict1) == m:
        count += 1

print(count)
