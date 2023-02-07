import os, time, random


def type():
  choices = ("Human", "Elf", "Wizard", "Orc")
  choice = random.choice(choices)
  return choice


def sliced_dice():
  six_side = random.randint(1,6)
  twelve_side = random.randint(1,12)
  side_roll = six_side * twelve_side
  return side_roll


def health():
  health = (sliced_dice() / 2) + 10
  return health


def strength():
  strength = (sliced_dice() / 2) + 12
  return strength

play_again = "yes"
while play_again == "yes":
  os.system("clear")
  print("Character Builder")
  char = input("Name your legend: ")
  print("Character Type (Human, Elf, Wizard, Orc):")
  print(type())
  print()
  time.sleep(1)
  print(char)
  time.sleep(1)
  print("HEALTH:", round(health()))
  time.sleep(1)
  print("STRENGTH:", round(strength()))
  print()
  time.sleep(1)
  print("May your name go down in legend...")
  time.sleep(1)
  print()
  play_again = input("Retry?: ")

  if play_again == "no":
    break
    time.sleep(1)
    exit()

