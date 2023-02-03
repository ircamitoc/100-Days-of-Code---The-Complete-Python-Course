print("How many seconds are there in a year?")
print("---")

l_year = 366
year = 365
minutes = 60
seconds = 60
hours = 24

question = input("Is it a leap year? [Y/N]: ")
if question == "Y" or question == "y":
    leap_year = (l_year * hours) * (minutes * seconds)
    print("There are",leap_year,"seconds in a leap year.")
elif question == "N" or question == "n":
    not_leap_year = (year * hours) * (minutes * seconds)
    print("There are",not_leap_year,"seconds in a year.")
else:
    print("Please indicate Y if yes or N if no.")
