# бесполезные кнопки

from tkinter import *
# создание базового окна
root = Tk()
root.title("Бесполезные кнопки")
root.geometry("200x85")
# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()
# создание кнопки внутри рамки
bttn1 = Button(app, text="Я ничего не делаю!")
bttn1.grid()
# создание второй кнопки внутри рамки
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="И я тоже!")
# создание третьей кнопки внутри рамки
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "И я!"
# старт событийного окна
root.mainloop()
