import datetime

a = datetime.datetime(2025, 2, 16, 16, 30, 50)
b = datetime.datetime(2025, 2, 15, 14, 20, 40)

difference = a - b

print(int(difference.total_seconds()))