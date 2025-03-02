import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

number = 25100
delay_ms = 2123

delayed_square_root(number, delay_ms)
