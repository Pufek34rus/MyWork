from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QAction
import random
import sys
from testo import As


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
        self.labelname = QLabel(self)
        self.intername = QLabel(self)
        self.label = QLabel(self)
        self.input = QLineEdit(self)
        self.button = QPushButton("Принять", self)
        self.button1 = QPushButton("Камень", self)
        self.button2 = QPushButton("Ножницы", self)
        self.button3 = QPushButton("Бумага", self)

    def bar(self):
        self.statusBar()
        menubar = self.menuBar()
        MenuGame = menubar.addMenu('Играть')
        MenuEx = menubar.addMenu('Выход')
        exitAction = QAction('Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Вызод из игры')
        exitAction.triggered.connect(sys.exit)
        GameAction = QAction("Начать игру",self)
        GameAction.setShortcut('Ctrl+N')
        GameAction.setStatusTip("Начало новой игры")
        GameAction.triggered.connect(As)
        MenuGame.addAction(GameAction)
        MenuEx.addAction(exitAction)

    def ACTION(self):
        self.input.textChanged.connect(self.labelname.setText)

        self.button.clicked.connect(As)
        self.button1.hide()
        self.button1.clicked.connect(As.testo2000)
        self.button2.hide()
        self.button2.clicked.connect(As.testo2001)
        self.button3.hide()
        self.button3.clicked.connect(As.testo2002)
        self.labelname.hide()
        self.intername.setText("Введите имя")
        self.button1.setIcon(QIcon("noj.jpg"))

    def GEO(self):
        self.setFixedSize(800, 600)
        self.intername.setGeometry(300, 210, 200, 20)
        self.labelname.setGeometry(0, 0, 200, 20)
        self.input.setGeometry(300, 230, 200, 20)
        self.button.setGeometry(300, 250, 200, 50)
        self.button1.setGeometry(150, 250, 100, 100)
        self.button2.setGeometry(350, 250, 100, 100)
        self.button3.setGeometry(550, 250, 100, 100)
        self.label.setGeometry(0, 0, 200, 100)

    def clickme(self):
        self.intername.hide()
        self.input.hide()
        self.labelname.show()
        self.button.hide()
        self.button1.show()
        self.button2.show()
        self.button3.show()




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
