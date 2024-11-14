print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:10")
from Graphics import rectangle, circle
from Graphics.subgraphics import cuboid,sphere

# Rectangle
length = int(input("Enter the length : "))
width = int(input("Enter the width : "))
print(f"Rectangle Area: {rectangle.area(length, width)}")
print(f"Rectangle Perimeter: {rectangle.perimeter(length, width)}")

# Circle
radius = int(input("Enter the radius : "))
print(f"Circle Area: {circle.area(radius)}")
print(f"Circle Perimeter: {circle.perimeter(radius)}")

# Cuboid
height = int(input("Enter the height : "))
print(f"Cuboid Surface Area: {cuboid.area(length, width, height)}")
print(f"Cuboid Perimeter: {cuboid.perimeter(length, width, height)}")

# Sphere
print(f"Sphere Surface Area: {sphere.area(radius)}")
print(f"Sphere Circumference: {sphere.perimeter(radius)}")
