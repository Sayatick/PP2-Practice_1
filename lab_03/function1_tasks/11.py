def palindrome_checker(element):
    reversed_e = element[::-1]
    if reversed_e == element:
        return True
    return False

word_1 = "madam"
word_2 = "sayat"

print(palindrome_checker(word_1))
print(palindrome_checker(word_2))