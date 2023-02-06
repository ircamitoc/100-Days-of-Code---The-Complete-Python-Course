print("Math Game")
print("---")
multiples = int(input(("Name your multiples > ")))
end = multiples*11
counter = 0
score = 0

for x in range(1, 11):
  correct_answer = x * multiples    
  print()
  print(x,"X",multiples)
  answer = int(input("Answer > "))
  if answer == correct_answer:
    counter += 1
    score += 1
    print("Great work! 🥳")
    continue
  elif answer != correct_answer:
    counter += 1
    print("""Nope! 😭 The answer was""", x)
    continue
  else:
    print("Invalid input. Please try again.\n")

if counter == 10:
  print("\nYou got a perfect score !")
  exit()
else:
  print("\nYou scored", score, "out of 10!")
  exit()