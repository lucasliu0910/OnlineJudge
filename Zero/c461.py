a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

check_and = False
check_or = False
check_xor = False

if c == 1:
  if a != 0 and b != 0:
    check_and = True
    check_or = True
  elif (a == 0 and b != 0) or (a != 0 and b == 0):
    check_or = True
    check_xor = True
  elif a == 0 and b == 0:
    pass

if c == 0:
  if a != 0 and b != 0:
    check_xor = True
  elif (a == 0 and b != 0) or (a != 0 and b == 0):
    check_and = True
  elif a == 0 and b == 0:
    check_and = True
    check_or = True
    check_xor = True

if check_and:
  print("AND")
if check_or:
  print("OR")
if check_xor:
  print("XOR")
if check_and == False and check_or == False and check_xor == False:
  print("IMPOSSIBLE")
