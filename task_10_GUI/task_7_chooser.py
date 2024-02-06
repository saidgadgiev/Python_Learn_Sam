# Демонстрируем применение флажков
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает элоементы, с помощью которых пользователь будет выбирать"""
        Label(self, text="Укажите ваши любимые жанры кино").grid(row=0, column=0, sticky=W)
        Label(self, text="Выберите все что вам по вкусу: ").grid(row=1, column=0, sticky=W)
        # Флажок комедия
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text="Комедия",
                    variable=self.likes_comedy,
                    command=self.update_text).grid(row=2, column=0, sticky=W)

        # Флажок драма
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text="Драма",
                    variable=self.likes_drama,
                    command=self.update_text).grid(row=3, column=0, sticky=W)

        # Флажок фильм о любви
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text="Комедия",
                    variable=self.likes_romance,
                    command=self.update_text).grid(row=4, column=0, sticky=W)
        # Текстовая область с результатами
        self.result_txt = Text(self, width=40, height=5, wrap=WORD)
        self.result_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = ""
        if self.likes_comedy.get():
            likes += "Вам нравятся комедии.\n"
        if self.likes_drama.get():
            likes += "Вас привлекает жанр Драмы.\n"
        if self.likes_romance.get():
            likes += "Вам по вкусу книги о любви."
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, likes)


# Основная часть
root = Tk()
root.title("Долгожитель")
root.geometry("300x150")
app = Application(root)
root.mainloop()
