# -99 -10 0 1 89  target:80

# -111 -99 0 80 111

# 0,4,mid=2
# 3,4,mid=3
# 4,4,mid=4
# 4,3


def binarySearch(in_list,target):
  left = 0
  right = len(in_list)-1
  if (len(in_list) == 1 and in_list[0] != target) or (target < in_list[0]) or (target > in_list[len(in_list)-1]):
    print("0")
  else:
    while left <= right:
      mid = (left+right)//2
      if in_list[mid] == target:
        print(mid+1)
        break
      elif in_list[mid] <= target:
        left = mid + 1
      elif in_list[mid] >= target:
        right = mid - 1
    if left > right:
      print("0")
n,k = map(int,input().split())
data = [i for i in map(int,input().split())]
key = [i for i in map(int,input().split())]

for i in key:
  binarySearch(data,i)
