# Read marks from standard input
marks = int(input("Enter marks: "))

# Check and assign grade based on marks
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

#output
#Enter marks: 85
#Grade: B
