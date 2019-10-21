from math import sqrt


def Letter_To_Number(w):
    number = 0
    for letter in w:
        if letter == '"':
            continue
        number += ord(letter) - ord('A') + 1
    return number


with open("p042_words.txt", 'r') as file_names:
    data = file_names.read().split(',')
    data = [word.strip('"') for word in data]
    file_names.close()

word_value = 0
counter = 0
for word in data:
    word_value = Letter_To_Number(word)
    if sqrt(8 * word_value + 1) == int(sqrt(8 * word_value + 1)):
        counter += 1
print(counter)
