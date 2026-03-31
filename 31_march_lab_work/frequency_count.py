# Input string
text = input("Enter a string: ")

# Empty dictionary
freq = {}

# Counting frequency
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Output result
print("Character Frequency:", freq)

#output
#Enter a string: hello
#{'h': 1, 'e': 1, 'l': 2, 'o': 1}
