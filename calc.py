x=int(input("Enter the num1\n:"))
y=int(input("Enter the num2\n:"))
choice=int(input("Enter your choice\n:"))
if(choice==1):
    print("Sum is",x+y)
elif(choice==2):
    print("Sub is",x-y)
elif(choice==3):
    print("Mul is",x*y)
elif(choice==4):
    print("Div is",x/y)
else:
    print("Invalid choice")
print("--------------------")
