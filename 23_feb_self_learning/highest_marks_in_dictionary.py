# Dictionary of students and marks
marks = {"Rahul": 85, "Ankit": 90, "Neha": 88}

# Finding highest marks
topper = max(marks, key=marks.get)

print("Topper:", topper)

#output
#Topper: Ankit
