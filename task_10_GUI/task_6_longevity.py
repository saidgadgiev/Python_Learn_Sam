# Демонстрируем текстовое поле
from tkinter import *


class Application(Frame):
    """GUI - поле"""
    def __init__(self, master):
        """Инициализируем рамку."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создаем кнопку, текстовое поле и текстовую область."""
        # метка инструкции
        self.inst_lbl = Label(self, text="Чтобы узнать секрет долголетия, введите пароль")
        self.inst_lbl.grid(row=0, column=0, columnspan=3, sticky=W)
        # метка около поля ввода пароля
        self.pw_lbl = Label(self, text="Пароль: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        # Текстовое поле для ввода пароля
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=2, column=1, sticky=W)
        # кнопка отправки значения
        self.submit_bttn = Button(self, text="Узнать секрет", command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)
        # создание текстовой области, в которую будет введен ответ
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        """В зависимости от введенного пароля отвечает разными сообщениями."""
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Чтобы дожить до 100 лет нужно вести здоровый образ жизни"
        else:
            message = "Вы ввели не правильный пароль"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


# Основная часть
root = Tk()
root.title("Долгожитель")
root.geometry("300x150")
app = Application(root)
root.mainloop()

