# Program to print all prime numbers between 1 and N (Easy version)

# Take input from user
n = int(input("Enter value of N: "))

print("Prime numbers between 1 and", n)

# Loop through numbers from 2 to N
for num in range(2, n + 1):
    count = 0   # Variable to count divisors

    # Check divisibility from 1 to num
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    # A prime number has exactly 2 divisors (1 and itself)
    if count == 2:
        print(num, end=" ")

  #output
  #Enter value of N: 20
#Prime numbers between 1 and 20
#2 3 5 7 11 13 17 19
