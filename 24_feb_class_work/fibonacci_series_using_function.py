 Function to generate Fibonacci series up to n terms
def fibonacci_series(n):
    a = 0  # First term
    b = 1  # Second term
    series = []  # List to store Fibonacci numbers
    
    # Loop to generate n terms
    for _ in range(n):
        series.append(a)  # Add current term to series
        c = a + b         # Calculate next term
        a = b             # Update a
        b = c             # Update b
    
    return series  # Return the list of Fibonacci numbers

# Read number of terms from the user
n_terms = int(input("Enter the number of terms: "))

# Call the function and print the Fibonacci series
print("Fibonacci series:")
print(fibonacci_series(n_terms))

#output
#Enter the number of terms: 7
#Fibonacci series:
#[0, 1, 1, 2, 3, 5, 8]
