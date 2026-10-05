# M6P3 - CD interest rate based on principle AND years to maturity
principle = float(input("Enter principle amount of CD: "))
years = int(input("Enter years to maturity: "))

if principle > 100000 and years == 5:
    rate = 0.06
elif principle >= 50000 and principle <= 100000 and years == 10:
    rate = 0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principle * rate

print(f"{'Principle:':<22}${principle:>14,.2f}")
print(f"{'Interest Rate:':<22}{rate * 100:>14.2f}%")
print(f"{'First Year Interest:':<22}${interest:>14,.2f}")
