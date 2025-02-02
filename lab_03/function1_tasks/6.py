def word_reverse(words):
    splitted_list_words = words.split()
    reversed_words = ' '.join(reversed(splitted_list_words))
    return reversed_words

words = input("Enter your word: ")

print(word_reverse(words))