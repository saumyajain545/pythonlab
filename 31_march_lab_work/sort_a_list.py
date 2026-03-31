# Input list of tuples
students = [("Aman", 75), ("Riya", 85), ("Karan", 65), ("Neha", 90)]

# Sort based on marks (second element)
sorted_list = sorted(students, key=lambda x: x[1])

# Output result
print("Sorted List:", sorted_list)

#output
#Sorted List: [('Karan', 65), ('Aman', 75), ('Riya', 85), ('Neha', 90)]
