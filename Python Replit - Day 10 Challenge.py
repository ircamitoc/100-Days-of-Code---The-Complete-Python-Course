print("Bill Payment")
print("---")

total_bill  = float(input("Total: "))
tip = int(input("Tip: "))
numberOfPeople = int(input("How many people: "))
answer = (total_bill + tip) / numberOfPeople
print("Your total amount is", round(answer))