n = int(input())
d = int(input())

list1 = []
for _ in range(n):
    list2 = [int(i) for i in input().split()]
    list1.append(list2)

##print(list1)

#測試資料第一組
#n_1 = 5
#d_1 = 0
#list1_1 = [[3, 4, 2, 1, 4], [4, 2, 3, 8, 9], [2, 1, 9, 5, 6], [4, 2, 3, 7, 8], [1, 2, 6, 4, 3]]

#測試資料第二組
#n_2 = 3
#d_2 = 1
#list1_2 = [[4, 1, 2], [3, 0, 5], [6, 7, 8]]

##[[4, 1, 2],
## [3, 0, 5],
## [6, 7, 8]]
##從 (3//2=1,3//2=1)=0 開始
##d為1表示向上
##(1,1)=0
##1上(0,1)=1
##2右(0,2)=2
##3下(1,2)=5
##3下(2,2)=8
##0左(2,1)=7
##0左(2,0)=6
##1上(1,0)=3
##1上(0,0)=4
##
##[[3, 4, 2, 1, 4],
## [4, 2, 3, 8, 9],
## [2, 1, 9, 5, 6],
## [4, 2, 3, 7, 8],
## [1, 2, 6, 4, 3]]
##從 (5//2=2,5//2=2)=9 開始
##d為0表示向左
##(2,2)9
##0左(2,1)1
##1上(1,1)2
##2右(1,2)3
##2右(1,3)8
##3下(2,3)5
##3下(3,3)7
##0左(3,2)3
##0左(3,1)2
##0左(3,0)4
##1上(2,0)2
##1上(1,0)4
##1上(0,0)3
##2右(0,1)4
##2右(0,2)2
##2右(0,3)1
##2右(0,4)4
##3下(1,4)9
##3下(2,4)6
##3下(3,4)8
##3下(4,4)3
##0左(4,3)4
##0左(4,2)6
##0左(4,1)2
##0左(4,0)1

#n = n_1

#d = d_1

if d == 0 or d == 2:
    d_begin = [0,2]
else:
    d_begin = [1,3]

#list1 = list1_1

r,c = n//2,n//2

def createRoute(d,k): #輸入d,k，加入k個d到list:move
    for _ in range(k):
        move.append(d)
            
move = []

for k in range(1,n):
    check = True
    for l in range(4):
        #print(f"k=={k},l=={l}")
        #print(f"d={d},d_begin={d_begin}")
        #print(f"check={check}")
        #print(f"move={move}")
        #print("")
        if check == False:
            break
        createRoute(d,k)
        d = (d+1)%4
        if d in d_begin:
            check = False
            break

createRoute(d,k)

#print(move)

for i in move:
    print(list1[r][c],end="")
    if i == 0:
        c = c -1
    elif i == 1:
        r = r-1
    elif i == 2:
        c = c+1
    elif i == 3:
        r = r+1
print(list1[r][c],end="")
