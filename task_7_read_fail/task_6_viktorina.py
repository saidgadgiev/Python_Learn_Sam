import sys


def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Не возможно открыть файл", file_name, ". Работа программы будет завершена\n", e)
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла"""
    line = the_file.readline()
    line = line.replace("/", "\n")

    # print(f"\n\nstart\t{line}\tfinish\n\n")

    return line


def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    category = next_line(the_file)
    question = next_line(the_file)
    # print(f"\n\nstart\t{question}\tfinish\n\n")
    # print(f"\n\nstart\t{next_line(the_file)}\tfinish\n\n")

    answers = []
    for i in range(4):
        # print(f"\n\nstart\t{next_line(the_file)}\tfinish\n\n")
        answers.append(next_line(the_file))
        correct = next_line(the_file)
        # if correct:
        #     correct = correct[0]
        #     explanation = next_line(the_file)
    print(f"\n\nstart\t{answers}\tfinish\n\n")

    print(f"\n\nstart\t{correct}\tfinish\n\n")

    return category, question, answers#, correct, explanation


def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")


def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)

    # print(f"\n\nstart\t{title}\tfinish\n\n")

    welcome(title)
    score = 0

# Извлечение первого блока
    category, question, answers, correct, explanation = next_block(trivia_file)

    # print(f"\n\nstart\t{answers}\tfinish\n\n")

    while category:
        print(category)
        print(question)
        for i in range(4):
            # print("\n\n\n\n Finish")
            print("\t", i + 1, "-", answers[i])
        category = False
    # получение ответа
    answer = input("Ваш ответ: ")
    # проверка ответа
    if answer == correct:
        print("\nДа!", end=" ")
        score += 1
    else:
        print("\nНет.", end=" ")
    print(explanation)
    print("Счет:", score, "\n\n")

    # переход к следующему вопросу
    category, question, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос")
    print("На вашем счету", score)


main()
# text_file = open("trivia.txt", "r")
# next_line(text_file)