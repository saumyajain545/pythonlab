#find largest of three numbers
num1=input(print("enter first value:"))
num2=input(print("enter second value:"))
num3=input(print("enter third value:"))
#check if first number is greatest
if num1>num2 and num1>num3:
    print("first number is largest")
#check if second number is greatest
elif num2>num3 and num2>num1:
    print("second number is largest")
#third number is greatest 
else:
    print("third number is largest")

#output
#enter first value:10
#enter second value:30
#enter third value:20
#second number is greatest
