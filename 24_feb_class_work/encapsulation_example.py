# Program to demonstrate encapsulation

class Person:                           # Define class
    def __init__(self, name):           # Constructor
        self.__name = name              # Private variable

    def get_name(self):                 # Getter method
        return self.__name              # Return private variable


p = Person("Rahul")                     # Create object
print("Name:", p.get_name())            # Access private data using method

# Output Example
# Name: Rahul
