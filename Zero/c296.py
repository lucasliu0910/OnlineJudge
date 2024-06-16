idx = 0

def next_lucky(circle,M): #modify circle, no return
  global idx
  idx = (idx+(M-1)) % len(circle)
  circle.pop(idx)
  idx = idx % len(circle)

N,M,K=map(int,input().split())
circle=list(range(1,N+1))

for _ in range(K):
  next_lucky(circle,M)

print(circle[idx])
