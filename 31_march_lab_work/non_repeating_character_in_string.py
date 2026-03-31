# Input string
text = input("Enter a string: ")
# Count frequency using dictionary
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

# Find first non-repeating character
for char in text:
    if freq[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")

#output
#Enter a string: aabbcde
#First non-repeating character: c
