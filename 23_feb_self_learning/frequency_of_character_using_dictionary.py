# Input string
s = "banana"
freq = {}

# Counting frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

#output
#{'b': 1, 'a': 3, 'n': 2}
