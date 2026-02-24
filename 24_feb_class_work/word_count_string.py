# Program to count number of words in a string

text = input("Enter a sentence: ")        # Take sentence input from user

words = text.split()                     # Split sentence into list of words

count = len(words)                       # Count total words

print("Number of words:", count)         # Display word count

# Output Example
# Enter a sentence: Python is very easy
# Number of words: 4
