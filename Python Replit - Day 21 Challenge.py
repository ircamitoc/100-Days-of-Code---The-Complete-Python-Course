loan = 1000
for counter in range(10):
  loan += (loan*0.05)
  print("Year", counter+1, ":", round(loan,2))
  