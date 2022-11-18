import random
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Камень, Ножницы, Бумага!")
        name = ""

        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()

    def layout(self):
        self.grid = QGreedLayout()
        self.grid.setSpacing(10)
        self.setLayout(grid)

    def UiComponents(self):
        self.button1 = QPushButton("Камень", self)
        self.button1.hide()
        self.button1.setGeometry(0, 0, 600, 40)
        self.button1.clicked.connect(self.test1)
        self.button2 = QPushButton("Ножницы", self)
        self.button2.hide()
        self.button2.setGeometry(0, 40, 600, 40)
        self.button2.clicked.connect(self.test2)
        self.button3 = QPushButton("Бумага", self)
        self.button3.hide()
        self.button3.setGeometry(0, 80, 600, 40)
        self.button3.clicked.connect(self.test3)
        self.button = QPushButton("CLICK", self)
        self.button.setGeometry(0, 0, 600, 40)
        self.button.clicked.connect(self.clickme)

    def test1(self):
        self.game(1)
    def test2(self):
        self.game(2)
    def test3(self):
        self.game(3)
    def clickme(self):
        self.button.hide()
        self.button1.show()
        self.button2.show()
        self.button3.show()

    def game(self, choiсe):
        print(choiсe, choiсe, choiсe, choiсe, choiсe, choiсe,)
        var = ["Камень", "Ножницы", "Бумага"]
        run = "Да"
        self.choiсe = choiсe
        while run == "Да":
            while True:

                comp = random.randint(0, len(var) - 1)

                if choiсe == 1 and comp == 0:
                    print("Игрок: Камень", "\nКомпьютер: ", var[comp])
                    print("Ничья")
                elif choiсe == 2 and comp == 1:
                    print("Игрок: Ножницы", "\nКомпьютер: ", var[comp])
                    print("Ничья")
                elif choiсe == 3 and comp == 2:
                    print("Игрок: Бумага", "\nКомпьютер: ", var[comp])
                    print("Ничья")
                elif choiсe == 1 and comp == 2:
                    print("Игрок: Камень", "\nКомпьютер: ", var[comp])
                    print("Победа компьютера")
                elif choiсe == 1 and comp == 1:
                    print("Игрок: Камень", "\nКомпьютер: ", var[comp])
                    print("Победа Игрока")
                elif choiсe == 2 and comp == 0:
                    print("Игрок: Ножницы", "\nКомпьютер: ", var[comp])
                    print("Победа Компютера")
                elif choiсe == 2 and comp == 2:
                    print("Игрок: Ножницы", "\nКомпьютер: ", var[comp])
                    print("Победа Игрока")
                elif choiсe == 3 and comp == 0:
                    print("Игрок: Бумага", "\nКомпьютер: ", var[comp])
                    print("Победа Игрока")
                elif choiсe == 3 and comp == 1:
                    print("Игрок: Бумага ", "\nКомпьютер: ", var[comp])
                    print("Победа Компьютера")
                else:
                    print("Неверное значение \nИгрок: ",
                          choiсe, "\nКомпьютер: ", var[comp])
                break
            run = input("Начать заного? Да/Нет: ")
            if run == "Нет":
                print("Игра закрыта")
                While = False
            if run == "Да":
                print("Начата новая игра: ")


App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())
