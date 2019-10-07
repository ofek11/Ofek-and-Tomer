def Letter_To_Number(w):
    number = 0
    for letter in w:
        if letter == '"':
            continue
        number += ord(letter) - ord('A') + 1
    return number


with open("p022_names.txt", 'r') as file_names:
    data = file_names.read().split(',')
    data.sort()

i = 1
counter = 0
for word in data:
    counter += i * Letter_To_Number(word)
    i += 1
print(counter)
