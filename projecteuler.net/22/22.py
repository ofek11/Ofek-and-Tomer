def Letter_To_Number(w):
    c = 0
    for letter in w:
        if letter == '"':
            continue
        number = ord(letter) - ord('A') + 1
        c += number
    return c


with open("p022_names.txt", 'r') as file_names:
    data = file_names.read().split(',')
    data.sort()

i = 1
for word in data:
    counter = 0
    data[i - 1] = i * Letter_To_Number(word)
    i += 1
print(sum(data))
