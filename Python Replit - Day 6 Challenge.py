print("Computer Login")
print("-----")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "Ice" and password == "Ice":
  print("\n\033[1;32mWelcome, Administrator", username + "!")
elif username == "Kait" and password == "Kaitlyn":
  print("\n\033[1;32mWelcome, Student", username +"!")
else:
  print("\n\033[1;31mInvalid access for this PC.")
