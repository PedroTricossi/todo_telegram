from datetime import date

today = date.today()

d1 = today.strftime("%d.%m")
d2 = float(d1)
print("d1 =", d2)
