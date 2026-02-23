# Attendance list (1 = present, 0 = absent)
attendance = [1, 0, 1, 0, 0, 1]

# Count present days
present = attendance.count(1)

# Calculate attendance percentage
percentage = (present / len(attendance)) * 100
print("Attendance %:", percentage)

# Replace consecutive absences with warning
for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i + 1] == 0:
        attendance[i] = "Warning"

# Display updated attendance
print("Updated Attendance:", attendance)

#output
#Attendance %: 50.0
#Updated Attendance: [1, 0, 1, 'Warning', 0, 1]
