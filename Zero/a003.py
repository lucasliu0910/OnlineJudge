m,d = input().split()
s = (int(m)*2+int(d))%3

if s==0: print("普通")
elif s==1: print("吉")
else: print("大吉")
