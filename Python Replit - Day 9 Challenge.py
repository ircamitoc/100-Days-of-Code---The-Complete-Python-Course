print("\033[1;96mGeneration Generator")
print("---")

year = int((input("What year were you born?: ")))
if year >= 1925 and year <= 1946:
  print("\n\033[1;93mYou are born in", year, "- a Traditionalist!")
elif year >= 1947 and year <= 1964:
  print("\n\033[1;93mYou are born in", year, "- a Baby Boomer!")
elif year >= 1965 and year <= 1981:
  print("\n\033[1;93mYou are born in", year, "- Generation X!")
elif year >= 1982 and year <= 1995:
  print("\n\033[1;93mYou are born in", year, "- a Millenial!")
elif year >= 1996 and year <= 2015:
  print("\n\033[1;93mYou are born in", year, "- Generation Z!")
else:
  print("\n\033[1;31mPlease input numbers only.")