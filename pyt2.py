
# Multi-Plan Telecommunications Cost Optimization

print("=== TELECOMMUNICATION COST OPTIMIZATION ===")

name = input("Enter customer name: ")
data_usage = float(input("Enter monthly data usage (GB): "))
call_minutes = int(input("Enter monthly call minutes: "))

# Plan details: (name, data limit, call limit, monthly cost)
plans = [
    ("Basic Plan", 5, 200, 199),
    ("Standard Plan", 15, 500, 399),
    ("Premium Plan", 30, 1000, 599)
]

available_plans = []

for plan in plans:
    plan_name, data_limit, call_limit, cost = plan

    if data_usage <= data_limit and call_minutes <= call_limit:
        available_plans.append(plan)

print("\nCustomer:", name)

if len(available_plans) > 0:
    best_plan = available_plans[0]

    for plan in available_plans:
        if plan[3] < best_plan[3]:
            best_plan = plan

    print("Recommended Plan:", best_plan[0])
    print("Monthly Cost: Rs.", best_plan[3])
else:
    print("No plan satisfies your usage requirements.")
    print("Consider a plan with higher limits.")
