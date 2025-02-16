def trapezoid_area(a, b, height):
    return ((a + b) * height) / 2

height = 5
base1 = 5
base2 = 6

area = trapezoid_area(base1, base2, height)
print(f"Trapezoid Area: {area}")