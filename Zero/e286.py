team1_1 = [int(i) for i in input().split()]
team2_1 = [int(i) for i in input().split()]
team1_2 = [int(i) for i in input().split()]
team2_2 = [int(i) for i in input().split()]

team1_1_sum = sum(team1_1)
team2_1_sum = sum(team2_1)
team1_2_sum = sum(team1_2)
team2_2_sum = sum(team2_2)

print(f"{team1_1_sum}:{team2_1_sum}")
print(f"{team1_2_sum}:{team2_2_sum}")

if team1_1_sum > team2_1_sum and team1_2_sum > team2_2_sum:
  print("Win")
elif team1_1_sum < team2_1_sum and team1_2_sum < team2_2_sum:
  print("Lose")
else:
  print("Tie")
