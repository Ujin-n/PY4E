def compute_pay(h, r):
    if h <= 40:
        return (h * r)
    else:
        return ((40 * rate) + ((hrs - 40) * rate*1.5 ))


hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = compute_pay(hrs, rate)

print("Pay", pay)