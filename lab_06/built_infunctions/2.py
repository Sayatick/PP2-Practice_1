def count_letters(s):
    uppers = 0
    lowers = 0

    for char in s:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1

    return uppers, lowers

text = "Hello World!"
upper, lower = count_letters(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)