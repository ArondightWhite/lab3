import sys

i = int(input("Enter month number: "))

if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
    print(31, "days")
elif i == 4 or i == 6 or i == 9 or i == 11:
    print(30, "days")
elif i == 2:
    print(28, "days")
else:
    print("There is no such month!", file=sys.stderr)
exit(1)
