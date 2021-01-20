import sys
x = float(input("Enter 1st real number: "))
y = float(input("Enter 2nd real number: "))

if x**2 * y > x * y**2:
    U = (x**2 * y)**2
else:
    U = (x * y**2)**2
if x - y < x + 2 * y:
    U += (x - y)**2
else:
    U += (x + 2 * y)**2

print(f"U = {U:.2f}\nu = {max((x**2 * y),(x * y**2))**2+min((x - y), (x + 2 * y))**2}")
