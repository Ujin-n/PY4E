hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rage: "))

if hrs <= 40:
    pay = hrs * rate
else:
    pay = (40 * rate) + ((hrs - 40) * rate*1.5 )

print(pay)