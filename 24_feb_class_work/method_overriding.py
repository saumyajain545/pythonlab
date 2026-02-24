# Program to demonstrate method overriding

class Parent:                           # Parent class
    def show(self):                     # Parent method
        print("Parent class method")    # Print message


class Child(Parent):                    # Child class
    def show(self):                     # Overriding method
        print("Child class method")     # Print message


obj = Child()                           # Create child object
obj.show()                              # Call overridden method

# Output Example
# Child class method
