# Function to count vowels in a string
def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":  # Check if character is a vowel (case-insensitive)
            count += 1
    return count

# Read a string from the user
string = input("Enter a string: ")

# Call the function and print the number of vowels
print("Number of vowels in the string:", count_vowels(string))

#output
#Enter a string: Hello World
#Number of vowels in the string: 3
