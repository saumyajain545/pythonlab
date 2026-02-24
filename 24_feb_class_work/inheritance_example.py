# Program to demonstrate inheritance

class Animal:                           # Parent class
    def speak(self):                    # Method in parent class
        print("Animal speaks")          # Print message


class Dog(Animal):                      # Child class inheriting Animal
    def bark(self):                     # Method in child class
        print("Dog barks")              # Print message


d = Dog()                               # Create object of Dog
d.speak()                               # Call parent method
d.bark()                                # Call child method

# Output Example
# Animal speaks
# Dog barks
