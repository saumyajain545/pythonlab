# Program to remove punctuation from a string

import string                            # Import string module

text = input("Enter a sentence: ")       # Take sentence input

clean_text = ""                          # Initialize empty string

for char in text:                        # Loop through each character
    if char not in string.punctuation:   # Check if not punctuation
        clean_text = clean_text + char   # Add character to clean string

print("Without punctuation:", clean_text)  # Display result

# Output Example
# Enter a sentence: Hello, World!
