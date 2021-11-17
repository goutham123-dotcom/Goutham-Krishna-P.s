x=int(input("Enter the num1\n:"))
y=int(input("Enter the num2\n:"))
choice=input("Enter your choice\n:")
if(choice=='+'):
    print("Sum is",x+y)
elif(choice=='-'):
    print("Sub is",x-y)
elif(choice=='*'):
    print("Mul is",x*y)
elif(choice=='/'):
    print("Div is",x/y)
else:
    print("Invalid choice")
print("--------------------")
