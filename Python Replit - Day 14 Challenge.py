from getpass import getpass as input

print("""
E P I C   🪨  📃  ✂️   B A T T L E
""")
print("\nSelect your move (R, P or S)")
player_1 = input("Player 1 > ")
player_2 = input("Player 2 > ")
if player_1 == "R" and player_2 == "P":
    print("Player 1's Rock is smothered by Player 2's Paper!")
elif player_1 == "P" and player_2 == "R":
    print("Player 2's Rock is smothered by Player 1's Paper")
elif player_1 == "P" and player_2 == "S":
    print("Player 1's Paper is snipped by Paper 2's Scissors")
elif player_1 == "S" and player_2 == "P":
    print("Player 2's Paper is snipped by Player 1's Scissors")
elif player_1 == "S" and player_2 == "R":
    print("Player 1's Scissors is damaged by Player 1's Rock")
elif player_1 == "R" and player_2 == "S":
    print("Player 2's Scissors is damaged by Player 1's Rock")
else:
  print("Please input R, P, or S only.")