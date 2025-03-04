from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit, QLabel)
import sys
from calculate import Calculate

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

        self.signs = [['AC', '^', '%', '/'],'X','-','+',['S','0','.', '=']]

        buttons_layout = QVBoxLayout()
        counter = 7
        for row in range(0,5):
            row_layout = QHBoxLayout()
            for columns in range(0,4):
                if row == 0:
                    button = QPushButton(self.signs[row][columns])
                    button.clicked.connect(self.button_clicked)
                    row_layout.addWidget(button)
                elif row == 4:
                    button = QPushButton(self.signs[row][columns])
                    button.clicked.connect(self.button_clicked)
                    if columns == 3:
                        button.setObjectName('equals')
                    row_layout.addWidget(button)
                elif columns == 3:
                    button = QPushButton(self.signs[row])
                    button.clicked.connect(self.button_clicked)
                    row_layout.addWidget(button)
                else:
                    button = QPushButton(str(counter))
                    button.clicked.connect(self.button_clicked)
                    row_layout.addWidget(button)
                    counter += 1
            if not row == 0 and not row == 4:
                counter -= 6

            buttons_layout.addLayout(row_layout)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def button_clicked(self):
        button = self.sender()
        value = button.text()
        if value == "0" or value == '.':
            self.result_field.setText(self.result_field.text() + value)
        elif value not in self.signs[0] and value not in self.signs and value not in self.signs[4]:
            self.result_field.setText(self.result_field.text() + value)
        elif value == 'AC':
            self.restart()
        elif value != 'S' and value != '=':
            self.result_field.setText(self.result_field.text() + value)
        elif value == '=':
            calculate = Calculate(self.result_field.text())
            result = calculate.calculate()

    def restart(self):
        self.result_field.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
