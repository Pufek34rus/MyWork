from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
import random
import sys
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        self.button = QPushButton("Начать игру", self)
        self.button.clicked.connect(self.clickme)
        self.button1 = QPushButton("Камень", self)
        self.button1.hide()
        self.button1.clicked.connect(self.testo2000)
        self.button2 = QPushButton("Ножницы", self)
        self.button2.hide()
        self.button2.clicked.connect(self.testo2001)
        self.button3 = QPushButton("Бумага", self)
        self.button3.hide()
        self.button3.clicked.connect(self.testo2002)

        layout = QVBoxLayout()
        # layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        container = QWidget()
        container.setLayout(layout)
        self.setGeometry(100, 100, 600, 400)
        self.setCentralWidget(container)

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
