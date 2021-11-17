x=int(input("Enter the First Num\n:"))
y=int(input("Enter the Second Num\n:"))
z=int(input("Enter the third Num\n:"))
if(x>y):
    if(x>z):
        print("X is greater",x)
    else:
        print("Z is greater",z)
else:
    if(y>z):
        print("Y is greater",y)
    else:
        print("Z is Greater",z)
