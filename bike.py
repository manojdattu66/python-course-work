# Task 1: Take Bike Repairing Details as Input

# Customer details
customer_id = int(input("Enter Customer ID: "))
customer_name = input("Enter Customer Name: ")
bike_model = input("Enter Bike Model: ")
contact_number = input("Enter Contact Number: ")

# Service & Payment details
service_type = input("Enter Service Type (e.g., Engine Repair, Oil Change): ")
service_cost = float(input("Enter Total Service Cost: "))
discount = float(input("Enter Discount Amount: ₹"))
final_amount = service_cost - discount

# Create tuple for cost breakdown
cost_details = (service_cost, discount, final_amount)

# Discount percentage
discount_percentage = (discount / service_cost) * 100

# List of issues (comma-separated)
issues_reported = input("Enter Issues Reported (comma-separated): ").split(',')

# Set of services applied (avoids duplicates)
services_applied = set(input("Enter Services Applied (comma-separated): ").split(','))

# Emergency contact info (dictionary)
emergency_contact_name = input("Enter Emergency Contact Name: ")
emergency_contact_number = input("Enter Emergency Contact Number: ")
emergency_info = {
    "Name": emergency_contact_name,
    "Number": emergency_contact_number
}

# Task 2: Display Using Different Formatting Methods

# 1. Comma Separation
print("\n--- Using Comma Separation ---")
print("Customer ID, Name, Bike:", customer_id, customer_name, bike_model, sep=', ')

# 2. Percentage Formatting
print("\n--- Using Percentage Formatting ---")
print("Discount Applied: %.2f%%" % discount_percentage)

# 3. f-strings
print("\n--- Using f-strings ---")
print(f"Customer: {customer_name} (ID: {customer_id})")
print(f"Bike Model: {bike_model} | Service Type: {service_type}")
print(f"Service Cost: ₹{cost_details[0]:.2f}")
print(f"Discount: ₹{cost_details[1]:.2f} | Final Amount: ₹{cost_details[2]:.2f}")
print(f"Issues Reported: {', '.join([issue.strip() for issue in issues_reported])}")
print(f"Services Applied: {', '.join([s.strip() for s in services_applied])}")

# 4. .format() Method
print("\n--- Using .format() Method ---")
print("Emergency Contact: Name - {}, Number - {}".format(
    emergency_info["Name"], emergency_info["Number"]
))
