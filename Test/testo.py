import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
    QPushButton, QAction, QLineEdit, QMessageBox)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Тест'
        self.width = 1400
        self.height = 900
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        self.button = QPushButton('Показать', self)
        self.button.move(20, 80)

        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Введено', textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
