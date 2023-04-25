import math

class Geometry:
    def circle_area(self, radius):
        return math.pi * radius**2

    def circle_circumference(self, radius):
        return 2 * math.pi * radius

    def triangle_area(self, base, height):
        return 0.5 * base * height

    def square_area(self, side):
        return side**2

    def rectangle_area(self, length, width):
        return length * width

    def parallelogram_area(self, base, height):
        return base * height

    def trapezoid_area(self, base1, base2, height):
        return 0.5 * (base1 + base2) * height

# Example usage:
geometry = Geometry()
circle_area = geometry.circle_area(5)
circle_circumference = geometry.circle_circumference(5)
triangle_area = geometry.triangle_area(10, 5)
square_area = geometry.square_area(4)
rectangle_area = geometry.rectangle_area(4, 6)
parallelogram_area = geometry.parallelogram_area(4, 5)
trapezoid_area = geometry.trapezoid_area(4, 6, 5)

print("Circle area:", circle_area)
print("Circle circumference:", circle_circumference)
print("Triangle area:", triangle_area)
print("Square area:", square_area)
print("Rectangle area:", rectangle_area)
print("Parallelogram area:", parallelogram_area)
print("Trapezoid area:", trapezoid_area)
