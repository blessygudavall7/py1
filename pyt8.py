
# Student Performance Trend Analysis

print("=== STUDENT PERFORMANCE ANALYSIS ===")

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        mark = float(input("Enter marks for exam " + str(j + 1) + ": "))
        marks.append(mark)

    students.append((name, tuple(marks)))

print("\n========== PERFORMANCE REPORT ==========")

for student in students:
    name = student[0]
    marks = student[1]

    average = sum(marks) / len(marks)

    print("\nStudent:", name)
    print("Exam Marks:", marks)
    print("Average Marks:", round(average, 2))

    if marks[2] > marks[0]:
        print("Performance Trend: Improving")
    elif marks[2] < marks[0]:
        print("Performance Trend: Declining")
    else:
        print("Performance Trend: Stable")

    highest = max(marks)
    lowest = min(marks)

    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
