# Conservation
import pickle, shelve

print("\nПомещение списков на полку.")
S = shelve.open("pickles2.dat")


print("Консервация списка.")
S["variety"] = ["огурцы", "помидоры", "капуста"]
S["shape"] = ["целые", "кубиками", "соломкой"]
S["brand"] = ["Главпродукт", "Чумак", "Бондюэль"]

S.sync() # Убедимся что данные записаны

print("\nИзвлечение списков из файла полки: ")
print("торговые марки - ", S["brand"])
print("формы - ", S["shape"])
print("Виды овощей - ", S["variety"])

S.close()

