time = int(input())

time_us = time - 15

if time_us < 0:
  time_us += 24

print(time_us)
