x,y,z = map(int,input().split())

max = x

if y >= x and y >= z:
  max = y
elif z >= x and z >=y:
  max = z

print(max)
