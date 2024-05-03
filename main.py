from PySide6.QtCore import Qt
from inter.design import *
from PySide6.QtWidgets import QMainWindow, QApplication
import sys

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()
