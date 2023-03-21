
b=int(input("Enter the value of b:"))
c=0
d=0
while(b!=0):
  d=b%10
  c=c*10+d
  b=int(b/10)
print("The reverse value is",c)
