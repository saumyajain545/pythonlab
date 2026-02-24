# Program to create a simple class and object

class Student:                          # Define Student class
    def __init__(self, name, age):      # Constructor method
        self.name = name                # Assign name
        self.age = age                  # Assign age

    def display(self):                  # Method to display data
        print("Name:", self.name)       # Print name
        print("Age:", self.age)         # Print age


s1 = Student("Rahul", 20)               # Create object of Student
s1.display()                            # Call display method

# Output Example
# Name: Rahul
# Age: 20
