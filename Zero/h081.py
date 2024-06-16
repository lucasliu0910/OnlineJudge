from sys import stdin

n,d = map(int,stdin.readline().split())
price = [int(a) for a in stdin.readline().split()]

n_1,d_1 = 3,10
price_1 = [50,20,45]

n_2,d_2 = 6,10
price_2 = [30,20,45,38,10,20]

#n,d,price = n_2,d_2,price_2

profit = 0

hold = False

for i in range(0,len(price)):
    if i == 0:
        hold = True
        buy = price[i]
    elif hold == True and price[i] >= buy+d:
        hold = False
        sale = price[i]
        profit += price[i]-buy
    elif hold == False and price[i] <= sale-d:
        hold = True
        buy = price[i]
    if i == len(price)-1 and hold == True:
        hold = False

print(profit)
