counter = 1

while True:
  lyric = input("Never going to _____ you up. > ")
  if lyric == "give" or lyric == "Give":
    print("You got it")
  else:
    print("Nope, try again")
    counter += 1
  if lyric == "give":
    break

print("You got the correct lyrics in", counter, "attempt(s).")