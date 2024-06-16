n = int(input())

t = [0,0,0] #左轉、右轉、迴轉的次數

d = [] #紀錄每一步朝向的方位

xp,yp = 0,0

for i in range(n):
    x,y = map(int,input().split())
    if xp == x:
        if y-yp > 0:
            d.append("n")
        else:
            d.append("s")
    elif yp ==y:
        if x-xp > 0:
            d.append("e")
        else:
            d.append("w")
    xp,yp = x,y

#print(d)

for i in range(n-1):
    #print(f"i={i},d[i]={d[i]}")
    if d[i] == "n":
        if d[i+1] == "s":
            t[2] += 1
        elif d[i+1] == "e":
            t[1] += 1
        elif d[i+1] == "w":
            t[0] += 1
    elif d[i] == "s":
        if d[i+1] == "n":
            t[2] += 1
        elif d[i+1] == "e":
            t[0] += 1
        elif d[i+1] == "w":
            t[1] += 1
    elif d[i] == "e":
        if d[i+1] == "n":
            t[0] += 1
        elif d[i+1] == "s":
            t[1] += 1
        elif d[i+1] == "w":
            t[2] += 1
    elif d[i] == "w":
        if d[i+1] == "n":
            t[1] += 1
        elif d[i+1] == "s":
            t[0] += 1
        elif d[i+1] == "e":
            t[2] += 1

print(*t)
