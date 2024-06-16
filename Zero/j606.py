from sys import stdin

def change(S,P): #輸入舊字串S(string)、排列方法P(list)，輸出新字串(string)
    new = [0 for _ in range(K)]
    for i in range(K):
        new[P[i]-1] = S[i]
    new_str = ""
    for i in range(K):
        new_str += new[i]
    return new_str

##print(change("abac",[4,1,3,2]))

#K,Q,R = 5,4,1
##print(change("abcde",[2,1,3,5,4]))
##print(change("baced",[5,1,2,4,3]))
##print(change("acdeb",[4,1,2,3,5]))
##print(change("cdeab",[3,1,4,5,2]))

K,Q,R = map(int,stdin.readline().split())
S = str(stdin.readline())
S_record = []
for i in range(Q):
    P = [int(a) for a in stdin.readline().split()]
    #print(f"S={S}")
    #print(f"P={P}")
    S = change(S,P)
    S_record.append(S)

#print(S_record)

for i in range(R):
    for j in range(Q):
        print(S_record[j][i],end="")
    if i == R-1:
        pass
    else:
        print("")
