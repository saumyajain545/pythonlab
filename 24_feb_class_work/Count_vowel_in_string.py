# Read a string from standard input
sentence = input("Enter a string: ")

# Initialize count variable
count = 0

# Loop through each character in the string
for ch in sentence:
    # Convert character to lowercase and check if it is a vowel
    if ch.lower() in "aeiou":
        count += 1   # Increment count if vowel

# Print the total number of vowels
print("Number of vowels in the string:", count)

#Enter a string: Hello World
#Number of vowels in the string: 3
