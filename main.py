def middle_letters(word):
    length = len(word)

    if length % 2 == 0:
        middle1 = word[length // 2 - 1]
        middle2 = word[length // 2]
        return middle1 + middle2
    else:
        return word[length // 2]


# Ввод слова с клавиатуры
word = input("Введите слово: ")

# Вызов функции и вывод результата
result = middle_letters(word)
print(f"Результат: {result}")
