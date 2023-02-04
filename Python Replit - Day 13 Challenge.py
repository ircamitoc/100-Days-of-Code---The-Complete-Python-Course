print("Exam Grade Calculator")
print("---")
print()
name_of_exam = input("Name of Exam: ")
max_score = int(input("Max. Possible Score: "))
user_score = int(input("Your score: "))

number_score = float(user_score / max_score)
final = round(number_score, 2)
final_percent = round(float(user_score / max_score)*100, 2)

if final >= .90:
  print("You got a",  final_percent, "%", "which is an A+")
elif final >= .80 and final <= .89:
  print("You got a",  final_percent, "%", "which is a A")
elif final >= .70 and final <= .79:
  print("You got a",  final_percent, "%", "which is a B")
elif final >= .60 and final <= .69:
  print("You got a",  final_percent, "%", "which is a C")
elif final >= .50 and final <= .59:
  print("You got a",  final_percent, "%", "which is a D")
elif final >= 0 and final <= .49:
  print("You got a", final_percent, "%", "which is a U")
else:
  print("Please enter numbers only!")