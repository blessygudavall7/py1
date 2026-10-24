
# University Scholarship Allocation System

print("====================================")
print(" UNIVERSITY SCHOLARSHIP ALLOCATION ")
print("====================================")

# List to store student records
students = []

# Tuple containing scholarship categories
scholarships = ("Merit Scholarship", "Need-Based Scholarship")

# Number of students
n = int(input("Enter number of students: "))

# Loop to collect student details
for i in range(n):
    print("\nEnter details for Student", i + 1)

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter percentage: "))
    income = float(input("Enter annual family income (Rs.): "))

    # Scholarship eligibility
    if marks >= 90:
        scholarship = scholarships[0]
        amount = 20000
        status = "Eligible"

    elif marks >= 75 and income <= 300000:
        scholarship = scholarships[1]
        amount = 15000
        status = "Eligible"

    else:
        scholarship = "No Scholarship"
        amount = 0
        status = "Not Eligible"

    # Store student details in a list
    student = (name, roll_no, marks, income,
               scholarship, amount, status)

    students.append(student)

# Display scholarship results
print("\n========== SCHOLARSHIP RESULTS ==========")

for student in students:
    print("\nStudent Name:", student[0])
    print("Roll Number:", student[1])
    print("Percentage:", student[2], "%")
    print("Annual Family Income: Rs.", student[3])
    print("Scholarship:", student[4])
    print("Scholarship Amount: Rs.", student[5])
    print("Status:", student[6])

print("\nTotal students processed:", len(students))
print("=========================================")
