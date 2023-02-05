from getpass import getpass as input

print("""
E P I C   🪨  📃  ✂️   B A T T L E
""")

p1_score = 0
p2_score = 0
round = 0

while True:
    round += 1
    print("\nRound", round)
    print("\nSelect your move (R, P, or S)")
    player_1 = input("Player 1 > ")
    player_2 = input("Player 2 > ")
    if player_1 == "R" and player_2 == "R":
        print("Draw")
        print("\nPlayer 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
        continue
    if player_1 == "P" and player_2 == "P":
        print("Draw")
        print("\nPlayer 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
        continue
    if player_1 == "S" and player_2 == "S":
        print("Draw")
        print("\nPlayer 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
    if player_1 == "R" and player_2 == "P":
        print("\nPlayer 1's Rock is smothered by Player 2's Paper!")
        p2_score += 1
        print("Player 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
    elif player_1 == "P" and player_2 == "R":
        print("\nPlayer 2's Rock is smothered by Player 1's Paper")
        p1_score += 1
        print("Player 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
    elif player_1 == "P" and player_2 == "S":
        print("\nPlayer 1's Paper is snipped by Paper 2's Scissors")
        p2_score += 1
        print("Player 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
    elif player_1 == "S" and player_2 == "P":
        print("\nPlayer 2's Paper is snipped by Player 1's Scissors")
        p1_score += 1
        print("Player 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
    elif player_1 == "S" and player_2 == "R":
        print("Player 1's Scissors is damaged by Player 1's Rock")
        p2_score += 1
        print("Player 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)
    elif player_1 == "R" and player_2 == "S":
        print("\nPlayer 2's Scissors is damaged by Player 1's Rock")
        p1_score += 1
        print("Player 1 Score:", p1_score)
        print("Player 2 Score:", p2_score)

    if p1_score == 3:
        print("\nPlayer 1 wins with", p1_score, "points")
        break
    elif p2_score == 3:
        print("\nPlayer 2 wins with", p2_score, "points")
        break
    elif p1_score < 3 and p2_score < 3:
        continue
