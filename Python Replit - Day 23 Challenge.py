def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    if username == "david" and password == "baldies4life":
      print("Welcome to Replit!")
      break
      exit()
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue

print("REPLIT LOGIN SYSTEM")
login()