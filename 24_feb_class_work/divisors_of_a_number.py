# Read a number from standard input
num = int(input("Enter a number: "))

# Print divisors of the number
print("Divisors of", num, "are:")

# Loop from 1 to the number
for i in range(1, num + 1):
    # Check if i divides num completely
    if num % i == 0:
        print(i)

  #output
  #Divisors of 12 are:
#1
#2
#3
#4
#6
#12Enter a number: 12
  
