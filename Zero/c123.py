c = False #�T�{�O�_���Ĥ@����Jn

while True:

  n = int(input()) #3

  if n == 0:
    break
  elif n!=0 and c == True:
    print("")
  
  c = True

  while True:

    check = True

    trains = [i for i in range(1,n+1)] # �|���}�J���� 1 2 3

    expect = [i for i in map(int,input().split())] # �ݭn���� True:1,3,2 False:3,1,2
    #print(expect)

    if expect[0] == 0:
      break

    station = [0] # ���b��������

    for i in expect:
      #print(f"i={i}")
      while True:
        if i == station[-1]:
          station.pop()
          break
        elif i > station[-1]:
          station.append(trains.pop(0))
        elif i < station[-1]:
          check = False
          break
        #print(f"station={station}")
      if check == False:
        print("No")
        break
    else:
      print("Yes")
