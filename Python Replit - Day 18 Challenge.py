number = 1639285
counter = 1

print("Number Guesser")
print("---")
while True:
    answer = int(input("What is your guess: "))
    if answer < 0:
      print("Please enter positive values.")
      exit()
    elif answer < number:
        counter += 1
        print("Too low. Try again.\n")
    elif answer > number:
        counter += 1
        print("Too high. Try again.\n")
        continue
    elif answer == number:
        print("Correct!\n")
        counter += 1
        print("\nIt took you", counter, "guesses to get it correct!")
        break
    else:
        print("That is not a number I recognize.")