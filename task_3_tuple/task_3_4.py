begin_number = int(input("Введите начало поиска: "))
end_number = int(input("Введите конец поиска: "))
interval_search = int(input("Введите интервал поиска: "))

for i in range(begin_number, end_number, interval_search):
    print(i)