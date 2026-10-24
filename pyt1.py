
# Hospital Billing and Patient Classification System

print("======================================")
print(" HOSPITAL BILLING MANAGEMENT SYSTEM")
print("======================================")

# List to store patient records
patients = []

# Tuple containing patient categories
categories = ("Child", "Adult", "Senior Citizen")

# Number of patients
n = int(input("Enter number of patients: "))

# Loop to collect patient details
for i in range(n):
    print("\nEnter details for Patient", i + 1)

    name = input("Enter patient name: ")
    patient_id = input("Enter patient ID: ")
    age = int(input("Enter patient age: "))

    consultation = float(input("Enter consultation fee (Rs.): "))
    treatment = float(input("Enter treatment charges (Rs.): "))
    medicine = float(input("Enter medicine charges (Rs.): "))