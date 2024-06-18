in_list = [i for i in input().split(" ")]

def postfix(in_list):
  num = []
  for i in in_list:
    if i not in "+-*/":
      num.append(i)
    else:
      n2 = num.pop(-1)
      n1 = num.pop(-1)
      operation = str(n1)+str(i)+str(n2)
      num.append(eval(operation))
  return int(num[0])

print(postfix(in_list))
