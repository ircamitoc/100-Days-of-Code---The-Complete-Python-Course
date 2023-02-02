print("Are you a TRUE fan of Hololive?")
print("Take this quiz to find out!")
print()

idol = input("What is Gawr Gura's favorite idol?: ")
if idol == "Hatsune Miku":
  print("\n\033[1;34mIs that so?")
  song = input("Then what did Gura play that she claimed as the 'hardest song' in Project Diva?: ")
  if song == "Sadistic Music Factory":
    print("\n\033[1;32mSpot on!!!")
  elif song == "Popipo":
    print("\n\033[1;35mYou're so close.")
  else:
    print("\n\033[1;33mDo you even watch Gura???")
else:
  print("\n\033[1;31mIncorrect!!!!")