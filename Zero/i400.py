from sys import stdin

#還原第一步驟。輸入步驟二前的字串T(str)，輸出還原步驟一的字串(str)。
def part1(T,e):
    count = 0
    T_out = ""
    #計算出現1的次數
    for i in range(n):
        #print(f"i={i}")
        if e[i] == "1":
            count += 1
    #print(f"count={count}")
    #翻轉
    if count % 2 == 0:
        T_out = T
    else:
        if len(T) % 2 == 0:
            A = T[:len(T)//2]
            B = T[len(T)//2:]
            T_out = B + A
        else:
            A = T[:len(T)//2]
            B = T[len(T)//2+1:]
            C = T[len(T)//2]
            T_out = B + C + A
    #print(f"T_out={T_out}")
    return T_out
#m,n = 1,5
#part1("ADABC","10110")

#還原第二步驟。輸入步驟二後的字串T(str)及加密表e(str)，輸出還原步驟二的字串(str)。
def part2(T,e):
    S = ""
    for i in range(n,0,-1):
        idx = i-1 #idx值實為少1
        if e[idx] == "0":
            S = T[-1] + S
            T = T[0:len(T)-1]
        elif e[idx] == "1":
            S = S+ T[-1]
            T = T[0:len(T)-1]
        #print(f"S={S}, T={T}")
    #print(f"final: S={S}, T={T}")
    return part1(S,e)
##m,n = 1,5
##print(part2("CABAD","10110"))
##
##m,n = 3,6
##part2("RETYWQ","000000")

m,n = map(int,stdin.readline().split())

E = []
for _ in range(m):
    E.append(str(stdin.readline().strip()))
#print(f"E={E}")

T = str(stdin.readline().strip())
#print(f"T={T}")

if m == 1:
    T = part2(T,E[0])
else:
    for i in range(m-1,-1,-1):
        #print(f"E[i]={E[i]}")
        T = part2(T,E[i])
        #print(f"T={T}")

print(T)
