text = input("Введите слово: ")
text_invert = ""
for i in range(1, len(text)+1):
    text_invert += text[i * -1]
print(text_invert)
