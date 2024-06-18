def checker(in_str):

  tmp = []

  for c in in_str:

    if c == "(":
      tmp.append("(")
    
    elif c == "[":
      tmp.append("[")
    
    elif c == "]":
      try:
        k = tmp.pop(-1)
        #print(tmp)
        #print(f"k={k}")
        #print(tmp)
      except:
        return "No"
      if k == "[":
        pass
      else:
        return "No"
    
    elif c == ")":
      try:
        k = tmp.pop(-1)
      except:
        return "No"
      if k == "(":
        pass
      else:
        return "No"
  
  if len(tmp) == 0:
    return "Yes"
  else:
    return "No"

print(checker(str(input())))
