
# Examination Result and Grace-Mark Validation

print("=== EXAMINATION RESULT SYSTEM ===")

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        mark = float(input("Enter marks for subject " + str(j + 1) + ": "))
        marks.append(mark)

    students.append((name, tuple(marks)))

print("\n========== EXAM RESULTS ==========")

for student in students:
    name = student[0]
    marks = list(student[1])

    total = sum(marks)
    percentage = total / len(marks)

    # Sample rules: 35 marks required to pass each subject.
    # Grace marks: maximum 5 marks for one subject,
    # provided the student fails only one subject.
    failed = []

    for i in range(len(marks)):
        if marks[i] < 35:
            failed.append(i)

    grace_used = 0

    if len(failed) == 1:
        index = failed[0]
        required = 35 - marks[index]

        if 0 < required <= 5:
            marks[index] = 35
            grace_used = required

    if all(mark >= 35 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    print("\nStudent:", name)
    print("Original Marks:", student[1])
    print("Final Marks:", tuple(marks))
    print("Grace Marks Used:", grace_used)
    print("Total Marks:", sum(marks))
    print("Percentage:", round(sum(marks) / len(marks), 2), "%")
    print("Result:", result)
