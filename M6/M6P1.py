# M6P1 - Widget price, tax and total
quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

print(f"{'Extended Price:':<18}${extended_price:>14,.2f}")
print(f"{'Tax (7%):':<18}${tax:>14,.2f}")
print(f"{'Total:':<18}${total:>14,.2f}")
