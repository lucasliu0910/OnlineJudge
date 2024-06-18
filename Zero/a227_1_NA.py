def hanoi(n,a,b,c,num):
  if n == 1:
    print(f"Move ring {num} from {a} to {c}")
  else:
    hanoi(n-1,a,c,b,num-1)
    hanoi(1,a,b,c,num)
    hanoi(n-1,b,a,c,num-1)

n = int(input())

hanoi(n,"A","B","C",n)
