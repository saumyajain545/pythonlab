# Program to check whether two strings are anagrams

str1 = input("Enter first string: ")     # Take first string input
str2 = input("Enter second string: ")    # Take second string input

if sorted(str1) == sorted(str2):         # Compare sorted characters
    print("Anagram")                     # If equal, strings are anagram
else:                                    # Otherwise
    print("Not an Anagram")              # Not anagram

# Output Example
# Enter first string: listen
# Enter second string: silent
# Anagram
