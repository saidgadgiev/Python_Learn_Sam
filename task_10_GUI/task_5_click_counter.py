# счетчик шелчков
from tkinter import *


class Application(Frame):
    """GUI - приложение, которое подсчитывает количество нажатий кнопки."""
    def __init__(self, master):
        """Инициализирует рамку."""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 # количество нажатий
        self.create_widget()

    def create_widget(self):
        """Создает кнопку, на которой отображается количество совершенных нажатий."""
        self.bttn = Button(self)
        self.bttn["text"] = "Количество щелчков: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """Увеличивает количество нажатий на единицу и отображает его"""
        self.bttn_clicks += 1
        self.bttn["text"] = "Количество щелчков: " + str(self.bttn_clicks)


# Основная часть
root = Tk()
root.title("Количество щелчков")
root.geometry("200x85")
app = Application(root)
root.mainloop()
