import random

def infinity_dice():
  while True:
    sides = int(input("How many sides?: "))
    roll = random.randint(1, sides)
    print("You rolled", roll, "\n")
    choice = input("Roll again?: ")
    if choice == "yes" or choice == "Yes":
      print()
      continue
    elif choice == "no" or choice == "No":
      exit()


print("Infinity Dice 🎲")
print("----")
infinity_dice()
