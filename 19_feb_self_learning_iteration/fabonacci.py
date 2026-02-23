n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#output
#Enter number of terms: 5
#0 1 1 2 3
