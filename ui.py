from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit, QLabel)
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

if __name__ == "__main__":
    app = QApplication([sys.argv])
    window = Calculator()
    window.show()
    sys.exit(app.exec())
