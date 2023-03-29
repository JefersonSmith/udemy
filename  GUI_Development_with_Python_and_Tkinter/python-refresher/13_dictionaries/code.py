friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friends_ages["Bob"] = 20
friends_ages["Rolf"] = 23

print(friends_ages)

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]
print(friends[1]["age"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

if "Bob" in student_attendance:
    print(f'Bob: {student_attendance["Bob"]}')
else:
    print("Bob is not a student in this class.")

attendance_values = student_attendance.values()
print((sum(attendance_values) / len(attendance_values)))