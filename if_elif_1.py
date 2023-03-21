    #comapre three numbers
  
  a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if a>b & a>c:
  print("a is greater number :",a)
elif b>a & b>c :
    print("b is greater number :",b)
elif b==a & b==c :
    print("all are equal with each other")
else:
  print("c is greater number",c)
