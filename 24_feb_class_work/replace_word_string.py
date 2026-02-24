# Program to replace a word in a string

text = input("Enter a sentence: ")       # Take sentence input
old_word = input("Enter word to replace: ")   # Take word to replace
new_word = input("Enter new word: ")     # Take new word

updated_text = text.replace(old_word, new_word)   # Replace word

print("Updated sentence:", updated_text)          # Display updated sentence

# Output Example
# Enter a sentence: I like Python
# Enter word to replace: Python
# Enter new word: Java
# Updated sentence: I like Java
