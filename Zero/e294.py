#找出比n小的完全奇數
def smaller(n_input):
    for i in range(0,len(n_input)):
        if str(n_input[i]) in "2468":
            n_input[i] = n_input[i]-1
            for j in range(i+1,len(n_input)):
                n_input[j] = 9
            break
        elif str(n_input[i]) in "0":
            n_input[i] = 9
            for j in range(i+1,len(n_input)):
                n_input[j] = 9
            n_input.pop(i-1)
            break
    x = ""
    for i in n_input:
        x += str(i)
    return int(x)

#找出比n大的完全奇數
def bigger(n_input):
    for i in range(0,len(n_input)):
        #print(f"n[i]={n[i]}")
        if str(n_input[i]) in "02468":
            #print("enter")
            n_input[i] = n_input[i]+1
            for j in range(i+1,len(n_input)):
                n_input[j] = 1
            break
    x = ""
    for i in n_input:
        x += str(i)
    return int(x)

##n_1 = [1,3,2,5,6] #13199,13311
##n_2 = [1,0,0,1] #1111,999
##n_3 = [1,3,2,5,6]
##n_4 = [3,5,0,0,1]
##
##n = n_1

try:
    while True:
        x = str(input())

        #將輸入的數字轉成list
        n = []
        for i in x:
            n.append(int(i))

        #將輸入的數字轉成int
        n_int = ""
        for i in n:
            n_int += str(i)
        n_int = int(n_int)

         #將產生的list複製一份
        n_2 = []
        for i in n:
            n_2.append(i)

        a = smaller(n_2) #小於n的完全奇數
        b = bigger(n) #大於n的完全奇數
        #print(a)
        #print(b)

        #印答案
        if n_int-a >= b-n_int:
            print(b-n_int)
        else:
            print(n_int-a)
except EOFError:
    pass
