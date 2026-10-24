
# Smart Parking Fee Management

print("=== SMART PARKING MANAGEMENT ===")

vehicles = []

n = int(input("Enter number of vehicles: "))

for i in range(n):
    print("\nVehicle", i + 1)

    number = input("Enter vehicle number: ")
    vehicle_type = input("Enter type (bike/car): ").lower()
    hours = int(input("Enter parking hours: "))

    if hours <= 0:
        print("Invalid parking duration.")
        continue

    if vehicle_type == "bike":
        rate = 20
    elif vehicle_type == "car":
        rate = 50
    else:
        print("Unsupported vehicle type.")
        continue

    # Charge for each started hour
    fee = rate * hours

    # Discount for long parking
    if hours >= 8:
        discount = fee * 0.10
    else:
        discount = 0

    final_fee = fee - discount

    vehicles.append(
        (number, vehicle_type, hours, fee, discount, final_fee)
    )

print("\n========== PARKING REPORT ==========")

total_collection = 0

for vehicle in vehicles:
    print("\nVehicle Number:", vehicle[0])
    print("Vehicle Type:", vehicle[1])
    print("Parking Hours:", vehicle[2])
    print("Base Fee: Rs.", vehicle[3])
    print("Discount: Rs.", vehicle[4])
    print("Final Fee: Rs.", vehicle[5])

    total_collection += vehicle[5]

print("\nVehicles Parked:", len(vehicles))
print("Total Collection: Rs.", total_collection)