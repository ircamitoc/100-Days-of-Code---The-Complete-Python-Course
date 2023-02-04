exit = "no"

while exit == "no":
  animal = input("What animal do you want?: ")
  if animal == "Cow":
    print("A",animal,"goes moo")
  elif animal == "Lesser Spotted Lemur":
    print("Ummm...the",animal,"goes awooga.")
  else:
    print("Please enter an animal.")
  exit = input("Do you want to exit?: ")