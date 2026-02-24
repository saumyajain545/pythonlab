# Read the number of terms from standard input
n = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Counter to keep track of printed terms
count = 0

# Generate Fibonacci series using while loop
while count < n:
    print(a)
    c = a + b        # Calculate next term
    a = b            # Update first term
    b = c            # Update second term
    count = count + 1

#output
#Enter the number of terms: 7
#0
#1
#1
#2
#3
#5
#8
