print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:1")

day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year (e.g., 2024): "))


print("The date is",day,"-",month,"-",year)


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(" is leap year.")
else:
    print(" not a leap year.")
