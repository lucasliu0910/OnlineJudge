k = int(input())
s = str(input())

##k_1, s_1 = 1, "aBBdaaa" #ans: 2
##k_2, s_2 = 3, "DDaasAAbbCC" #ans: 3
##k_3, s_3 = 2, "aafAXbbCDCCC" #ans: 8
##k_4, s_4 = 3, "DDaaAAbbCC" #ans: 0
##k_5, s_5 = 2, "DDaaGaaDDccLLL" #ans: 8
##
##k, s = k_5, s_5

#掃一遍字串，找出每個位置是大寫或小寫，紀錄在一個陣列
#eg. (k=2) aafAXbbCDCCC -> [0,0,0,1,1,0,0,1,1,1,1,1]
def fun1(s):
    list1 = []
    for i in s:
        if i.isupper():
            list1.append(1)
        else:
            list1.append(0)
    return(list1)
#print(fun1(s))

#找出每一個連續大(小)寫片段的長度並記錄在陣列
#eg. [0,0,0,1,1,0,0,1,1,1,1,1] -> [3,2,2,5]
def length(list1):
    list2 = []
    c = list1[0]
    count = 0
    for i in list1:
        if i == c:
            count += 1
        else:
            list2.append(count)
            count = 0
            c = i
            count += 1
    list2.append(count)
    return list2
#print(length(fun1(s)))

#模擬從每一個位置開始算的狀況，若大於等於k則count+=k，將count加入ans，最後答案為max(ans)
def find(k,s):
    list1 = length(fun1(s))
    ans = []
    for x in range(0,len(list1)):
        count = 0
        check = False #檢查是否已經進入過第二個迴圈
        for i in range(x,len(list1)):
            #print(f"list1[i]={list1[i]}")
            if check == False:
                if list1[i] >= k:
                    count += k
                    check = True
                else:
                    break
            else:
                if list1[i] == k:
                    count += k
                elif list1[i] > k:
                    count += k
                    break
                elif list1[i] < k:
                    break
        ans.append(count)
    #print(f"list1={list1}")
    #print(f"ans={ans}")
    return max(ans)

print(find(k,s))
