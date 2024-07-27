import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

#"pyuic5 -.ui file path-" on powershell is the command to turn ui files into source code and display in terminal.
#"pyuic5 -x -.ui file path- -o -.py file path-" is the command to create a python file of the source code.

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Application")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("This is label.")
        self.label.move(250, 250)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click Me")
        self.button.clicked.connect(self.clicked)

        self.show()

    def clicked(self):
        self.label.setText("You pressed the button.")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

window()
