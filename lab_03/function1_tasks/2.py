def to_celsius(x):
    return (5 / 9) * (x - 32)

fahrenheit = int(input("Fahrengeit: "))

print("in Celsiuis: ", to_celsius(fahrenheit))