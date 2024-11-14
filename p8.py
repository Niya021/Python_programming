print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:8")
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

num=int(input("enter a number:"))
print(factors(num))

area_square = lambda side: side ** 2
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height

side = float(input("\nEnter the side  of the square: "))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

print(f"Area of square:{area_square(side)}")
print(f"Area of rectangle:{area_rectangle(length, width)}")
print(f"Area of triangle:{area_triangle(base, height)}")


