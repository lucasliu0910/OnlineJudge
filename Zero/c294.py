triangle = [int(i) for i in input().split()]
#triangle = [99,101,100]

triangle.sort()

print(*triangle)

c = triangle[2]
b = triangle[1]
a = triangle[0]

if a + b <= c:
  print("No")
elif a*a + b*b < c*c:
  print("Obtuse")
elif a*a + b*b == c*c:
  print("Right")
elif a*a + b*b > c*c:
  print("Acute")
