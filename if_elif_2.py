   # student attandance checking
  
attand=float(input("Enter your attandance in percentage:"))
sem=int(input("Enter your semester:"))
s=input("Enter your medical submission status:")
if attand>=75:
  print("Allowed in exam")
elif attand<75:
  if s=='submit':
    print("You are allowed on special permission. ")
  else:
    print("Not allowed")
