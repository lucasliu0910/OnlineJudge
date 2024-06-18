k = int(input())
score = 0

if k >= 40:
  score = 100
elif k >= 20:
  score = (k-20)*1+10*2+10*6
elif k >= 10:
  score = (k-10)*2+10*6
else:
  score = k*6

print(score)
