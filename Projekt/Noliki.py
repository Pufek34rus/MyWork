from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QAction
import random
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Камень, ножницы, бумага!"
        self.UI()
        self.ACTION()
        self.GEO()
        self.bar()

    def UI(self):
        self.setWindowTitle(self.title)
        self.lblnameShow = QLabel(self)
        self.lblnameSet = QLabel(self)
        self.lblgame = QLabel(self)
        self.inputName = QLineEdit(self)
        self.btnStart = QPushButton("Принять", self)
        self.btnStone = QPushButton("Камень", self)
        self.btnNoj = QPushButton("Ножницы", self)
        self.btnPapper = QPushButton("Бумага", self)

    def bar(self):
        self.statusBar()
        menubar = self.menuBar()
        MenuGame = menubar.addMenu('Играть')
        MenuEx = menubar.addMenu('Выход')
        exitAction = QAction('Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Вызод из игры')
        exitAction.triggered.connect(sys.exit)
        GameAction = QAction("Начать игру", self)
        GameAction.setShortcut('Ctrl+N')
        GameAction.setStatusTip("Начало новой игры")
        GameAction.triggered.connect(self.Start)
        MenuGame.addAction(GameAction)
        MenuEx.addAction(exitAction)

    def ACTION(self):

        self.btnStart.clicked.connect(self.Start)
        self.btnStone.hide()
        self.btnStone.clicked.connect(self.testo2000)
        self.btnNoj.hide()
        self.btnNoj.clicked.connect(self.testo2001)
        self.btnPapper.hide()
        self.btnPapper.clicked.connect(self.testo2002)
        self.lblnameSet.setText("Введите имя")
        self.btnStone.setIcon(QIcon("noj.jpg"))

    def GEO(self):
        self.setFixedSize(800, 600)
        self.lblnameSet.setGeometry(300, 210, 200, 20)
        self.lblnameShow.setGeometry(100, 200, 200, 20)
        self.inputName.setGeometry(300, 230, 200, 20)
        self.btnStart.setGeometry(300, 250, 200, 50)
        self.btnStone.setGeometry(150, 250, 100, 100)
        self.btnNoj.setGeometry(350, 250, 100, 100)
        self.btnPapper.setGeometry(550, 250, 100, 100)
        self.lblgame.setGeometry(0, 0, 200, 100)

    def Start(self):
        self.lblnameShow.setText(self.inputName.text())
        self.lblnameSet.hide()
        self.inputName.hide()
        self.btnStart.hide()
        self.btnStone.show()
        self.btnNoj.show()
        self.btnPapper.show()

    def testo2000(self):
        var = ["Камень", "Ножницы", "Бумага"]
        comp = random.randint(0, len(var) - 1)

        if comp == 0:
            var = var[comp]
            lblsource = f"Игрок: Камень \nКомпьютер: {var}\nНичья"
            self.lblgame.setText(lblsource)
        if comp == 2:
            var = var[comp]
            lblsource = f"Игрок: Камень \nКомпьютер: {var}\nПобеда компьютера"
            self.lblgame.setText(lblsource)
        if comp == 1:
            var = var[comp]
            lblsource = f"Игрок: Камень \nКомпьютер: {var}\nПобеда игрока"
            self.lblgame.setText(lblsource)

    def testo2001(self):
        var = ["Камень", "Ножницы", "Бумага"]
        comp = random.randint(0, len(var) - 1)

        if comp == 0:
            var = var[comp]
            lblsource = f"Игрок: Ножницы \nКомпьютер: {var}\nПобеда компьютера"
            self.lblgame.setText(lblsource)
        if comp == 2:
            var = var[comp]
            lblsource = f"Игрок: Ножницы \nКомпьютер: {var}\nПобеда игрока"
            self.lblgame.setText(lblsource)
        if comp == 1:
            var = var[comp]
            lblsource = f"Игрок: Ножницы \nКомпьютер: {var}\nНичья"
            self.lblgame.setText(lblsource)

    def testo2002(self):
        var = ["Камень", "Ножницы", "Бумага"]
        comp = random.randint(0, len(var) - 1)

        if comp == 0:
            var = var[comp]
            lblsource = f"Игрок: Бумага \nКомпьютер: {var}\nПобеда игрока"
            self.lblgame.setText(lblsource)
        if comp == 2:
            var = var[comp]
            lblsource = f"Игрок: Бумага \nКомпьютер: {var}\nНичья"
            self.lblgame.setText(lblsource)
        if comp == 1:
            var = var[comp]
            lblsource = f"Игрок: Бумага \nКомпьютер: {var}\nПобеда компбютера"
            self.lblgame.setText(lblsource)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
