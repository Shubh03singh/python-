   # add the decimal equivalents of 1/2,1/3,1/4.......,1/10

a=0
s=0

for i in range(1,11):
    a=(1/i)
    s=(s+a)
print("The sum:",round(s,3))
