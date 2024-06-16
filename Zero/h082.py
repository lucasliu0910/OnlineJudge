from sys import stdin

n1,m1 = 4,1
S1 = [4,2,5,3]
T1 = [2,5,1,5]
rounds1 = [0,1,2,3] #[1,2,3,4]

n2,m2 = 4,5
S1 = [4,1,5,3]
T1 = [6,5,1,6]
rounds1 = [3,0,2,1] #[4,1,3,2]

a,m,S,T,rounds = n1,m1,S1,T1,rounds1

#輸入兩玩家之idx，判斷輸贏，改變其戰鬥及應變力值，輸出贏家、輸家之idx
def out(p1,p2):
    #print(f"S(start)={S},T(start)={T}")
    a = S[p1]
    b = T[p1]
    c = S[p2]
    d = T[p2]
    winner = 0
    #print(f"a={a},b={b},c={c},d={d}")
    if a*b >= c*d:
        #print("enter!")
        winner = p1
        loser = p2
        S[p1] = a+c*d//(2*b)
        T[p1] = b+c*d//(2*a)
        S[p2] = c+c//2#
        T[p2] = d+d//2
    else:
        #print("enter2!")
        winner = p2
        loser = p1
        S[p1] = a+a//2
        T[p1] = b+b//2
        S[p2] = c+a*b//(2*d)
        T[p2] = d+a*b//(2*c)
    #print(f"[winner,loser]={[winner,loser]}")
    #print(f"S(end)={S},T(end)={T}")
    return [winner,loser]
#print(out(0,1))
#print(S,T)
#print(out(2,1))

#輸入目前round順序，輸出淘汰完後，按勝利組和失敗組排列之新的round順序
def play(rounds):
    winner_group = []
    loser_group = []
    for i in range(0,len(rounds)-1,2):
        #print(i)
        result = out(rounds[i],rounds[i+1])
        winner,loser = result[0],result[1]
        winner_group.append(winner)
        lose_count[loser] += 1
        if lose_count[loser] < m:
            loser_group.append(loser)
    if len(rounds)%2 != 0:
        winner_group.append(rounds[-1])
    #print(f"rounds(new)={winner_group+loser_group}")
    #print(f"lose_count={lose_count}")
    return winner_group+loser_group
#play(rounds)
#play([1,3])

n,m = map(int,stdin.readline().split())
S = [int(a) for a in stdin.readline().split()]
T = [int(a) for a in stdin.readline().split()]
rounds = [int(a)-1 for a in stdin.readline().split()]
lose_count = [int(0) for a in range(n)]

#print(rounds)
while len(rounds) != 1:
    rounds = play(rounds)
print(rounds[0]+1)
#print(S,T)
#print(lose_count)
