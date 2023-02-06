import random

def roll_dice(sides):
  roll = random.randint(1, sides)
  return roll

def stats_generator():
  six_side = roll_dice(6)
  eight_side = roll_dice(8)
  sum = six_side * eight_side
  return sum

counter = 1
print("⚔️ Character Stats Generator ⚔️")
print()

more = "yes"
while more == "yes":
  print("\nPlayer", counter)
  warrior = input("Name your warrior: ")
  sum = str(stats_generator())
  print("Their health is:",sum,"hp\n")
  counter += 1
  more = input("Add another character? ")