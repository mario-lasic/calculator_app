from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit, QLabel)
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        self.createUI()

    def createUI(self):
        self.result_field = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.result_field)

        signs = [['AC', 'B', '%', '/'],'X','-','+',['S','0',',', '=']]

        buttons_layout = QVBoxLayout()
        counter = 1
        for row in range(0,5):
            row_layout = QHBoxLayout()
            for columns in range(0,4):
                if row == 0:
                    button = QPushButton(signs[row][columns])
                    row_layout.addWidget(button)
                elif row == 4:
                    button = QPushButton(signs[row][columns])
                    if columns == 3:
                        button.setObjectName('equals')
                    row_layout.addWidget(button)
                elif columns == 3:
                    button = QPushButton(signs[row])
                    row_layout.addWidget(button)
                else:
                    button = QPushButton(str(counter))
                    counter += 1
                    row_layout.addWidget(button)

            buttons_layout.addLayout(row_layout)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
