# Input string
s = "education"
count = 0

# Counting vowels
for ch in s:
    if ch in "aeiou":
        count += 1

print("Vowel count:", count)

#output
#Vowel count: 5
