#swap two number without third variable
#input of first number
num1=input(print("enter first value:"))
#input of second number
num2=input(print("enter second value:"))
#display value before swapping
print("before swapping")
print("value1:",num1)
print("value2:",num2)
#swapping 
num1=num1+num2-num1
num2=num1+num2-num2
#display value after swapping
print("after swapping")
print("value1:",num1)
print("value2:",num2)

#output
#enter first value:2
#enter second value:3
#before swapping
#value1:2
#value2:3
#after swapping
#value1:3
#value2:2
