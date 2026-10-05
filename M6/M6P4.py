# M6P4 - Concert ticket pricing by volume
tickets = int(input("Enter number of concert tickets: "))

if tickets >= 25:
    price = 50.00
elif tickets >= 10:
    price = 60.00
elif tickets >= 5:
    price = 70.00
else:
    price = 75.00

total = tickets * price

print(f"{'Number of Tickets:':<20}{tickets:>13}")
print(f"{'Price Per Ticket:':<20}${price:>12,.2f}")
print(f"{'Total Cost:':<20}${total:>12,.2f}")
