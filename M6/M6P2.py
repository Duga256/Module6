# M6P2 - Part number unit cost and total cost
part = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

if part == "10" or part == "55":
    unit_cost = 1.00
elif part == "99":
    unit_cost = 2.00
elif part == "80" or part == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

print(f"{'Part Number:':<16}{part:>14}")
print(f"{'Cost Per Unit:':<16}${unit_cost:>13,.2f}")
print(f"{'Total Cost:':<16}${total_cost:>13,.2f}")
