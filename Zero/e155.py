try:
  while True:
    n = int(input())
    if n == 0:
      break
    else:
      cards = [i for i in range(1,n+1)]
      dis = []
      while len(cards) >= 2:
        dis.append(cards.pop(0))
        cards.append(cards.pop(0))
      #print(*dis)
      print("Discarded cards:",end=" ")
      for i in dis:
        if i == dis[-1]:
          print(i,end="")
        else:
          print(i,end=", ")
      print("")
      print(f"Remaining card: {cards[0]}")
except:
  pass
