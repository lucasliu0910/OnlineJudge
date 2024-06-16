##A  -> 0 1 0 1
##B  -> 0 1 1 1
##C  -> 0 0 1 0
##D  -> 1 1 0 1
##E  -> 1 0 0 0
##F  -> 1 1 0 0

from sys import stdin

def find(data):
    if data == "0 1 0 1":
      return "A"
    elif data == "0 1 1 1":
       return "B"
    elif data == "0 0 1 0":
        return "C"
    elif data == "1 1 0 1":
        return "D"
    elif data == "1 0 0 0":
        return "E"
    elif data == "1 1 0 0":
        return "F"

for n in stdin:
    n = int(n)
    #print("==")
    ans = ""
    for _ in range(n):
        data = stdin.readline().strip()
        #print(f"data={data},type:{type(data)}")
        a = find(data)
        ans += a
    print(ans)
