import math

def func(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Input degree: "))

radians = func(degrees)
print("Output radian: " ,radians)