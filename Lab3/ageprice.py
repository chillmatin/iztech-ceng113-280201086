age = float(input("Age: "))
price = 3.0

if age < 6 or age > 60:
    price = 0
elif age >= 6 and age <= 18:
    price = price / 2

print("Price is", price,"TL")