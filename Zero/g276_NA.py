n,m,k = map(int,input().split())

pos = []
vec = []

for i in range(k):
    a,b,c,d = map(int,input().split())
    pos.append([a,b])
    vec.append([c,d])

bomb = []

def check():
    global bomb
    global pos
    global vec
    remove = [0*a for a in range(len(pos))]
    bomb_check = [0*a for a in range(len(bomb))]
    pos2 = []
    vec2 = []
    for i in range(len(pos)):
        if pos[i][0] > n-1 or pos[i][1] > m-1 or pos[i][0] < 0 or pos[i][1] < 0:
            remove[i] = 1
        if pos[i] in bomb:
            remove[i] = 1
            bomb_check.append(pos[i])
    for i in range(len(pos)):
        if remove[i] == 0:
            pos2.append(pos[i])
            vec2.append(vec[i])
    pos = pos2
    vec = vec2
    for i in bomb_check:
        while i in bomb:
            bomb.remove(i)

while len(pos) != 0:
    for i in range(len(pos)):
        x = pos[i][0]
        y = pos[i][1]
        bomb.append([x,y])
    for i in range(len(pos)):
        pos[i][0] = pos[i][0]+vec[i][0]
        pos[i][1] = pos[i][1]+vec[i][1]
    check()

bomb_ans = set(map(tuple,bomb))
print(len(bomb_ans))
