from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import random
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Камень, ножницы, бумага!"
        self.UI()
        self.ACTION()
        self.GEO()

    def UI(self):
        self.setWindowTitle(self.title)
        self.labelname = QLabel(self)
        self.intername = QLabel(self)
        self.label = QLabel(self)
        self.input = QLineEdit(self)
        self.button = QPushButton("Принять", self)
        self.button1 = QPushButton("Камень", self)
        self.button2 = QPushButton("Ножницы", self)
        self.button3 = QPushButton("Бумага", self)

    def ACTION(self):
        self.input.textChanged.connect(self.labelname.setText)

        self.button.clicked.connect(self.clickme)
        self.button1.hide()
        self.button1.clicked.connect(self.testo2000)
        self.button2.hide()
        self.button2.clicked.connect(self.testo2001)
        self.button3.hide()
        self.button3.clicked.connect(self.testo2002)
        self.labelname.hide()
        self.intername.setText("Введите имя")

    def GEO(self):
        self.setFixedSize(800, 600)
        self.intername.setGeometry(300,210,200,20)
        self.labelname.setGeometry(0, 0, 200, 20)
        self.input.setGeometry(300, 230, 200, 20)
        self.button.setGeometry(300, 250, 200, 50)
        self.button1.setGeometry(150, 250, 100, 100)
        self.button2.setGeometry(350, 250, 100, 100)
        self.button3.setGeometry(550, 250, 100, 100)
        self.label.setGeometry(0, 0, 100, 200)

    def clickme(self):
        self.intername.hide()
        self.input.hide()
        self.labelname.show()
        self.button.hide()
        self.button1.show()
        self.button2.show()
        self.button3.show()

    def testo2000(self):
        var = ["Камень", "Ножницы", "Бумага"]
        comp = random.randint(0, len(var) - 1)

        if comp == 0:
            var = var[comp]
            ELabel = f"Игрок: Камень \nКомпьютер: {var}\nНичья"
            self.label.setText(ELabel)
        if comp == 2:
            var = var[comp]
            ELabel = f"Игрок: Камень \nКомпьютер: {var}\nПобеда компьютера"
            self.label.setText(ELabel)
        if comp == 1:
            var = var[comp]
            ELabel = f"Игрок: Камень \nКомпьютер: {var}\nПобеда игрока"
            self.label.setText(ELabel)

    def testo2001(self):
        var = ["Камень", "Ножницы", "Бумага"]
        comp = random.randint(0, len(var) - 1)

        if comp == 0:
            var = var[comp]
            ELabel = f"Игрок: Ножницы \nКомпьютер: {var}\nПобеда компьютера"
            self.label.setText(ELabel)
        if comp == 2:
            var = var[comp]
            ELabel = f"Игрок: Ножницы \nКомпьютер: {var}\nПобеда игрока"
            self.label.setText(ELabel)
        if comp == 1:
            var = var[comp]
            ELabel = f"Игрок: Ножницы \nКомпьютер: {var}\nНичья"
            self.label.setText(ELabel)

    def testo2002(self):
        var = ["Камень", "Ножницы", "Бумага"]
        comp = random.randint(0, len(var) - 1)

        if comp == 0:
            var = var[comp]
            ELabel = f"Игрок: Бумага \nКомпьютер: {var}\nПобеда игрока"
            self.label.setText(ELabel)
        if comp == 2:
            var = var[comp]
            ELabel = f"Игрок: Бумага \nКомпьютер: {var}\nНичья"
            self.label.setText(ELabel)
        if comp == 1:
            var = var[comp]
            ELabel = f"Игрок: Бумага \nКомпьютер: {var}\nПобеда компбютера"
            self.label.setText(ELabel)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
