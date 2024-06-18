l,m = map(int,input().split())

ListL =[]

for i in range(0,l+1):
  ListL.append(i)
#print(ListL)

for i in range(m):
  a,b = map(int,input().split())
  for m in range(a,b+1):
    try:
      ListL.remove(m)
    except:
      pass

#print(ListL)

print(len(ListL))
