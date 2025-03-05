from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit, QLabel,
                               QGridLayout)
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

        self.signs = [['AC', '^', '%', '/'], 'X', '-', '+', ['0', '.', '=']]

        buttons_layout = QGridLayout()
        counter = 7
        for row in range(0, 5):
            for column in range(0, 4):
                if row == 0:
                    button = QPushButton(self.signs[row][column])
                    button.clicked.connect(self.button_clicked)
                    buttons_layout.addWidget(button, row, column)
                elif row == 4:
                    if column == 3:
                        print("HERE")
                        continue
                    else:
                        button = QPushButton(self.signs[row][column])
                        button.clicked.connect(self.button_clicked)
                        if column == 2:
                            button.setObjectName('equals')
                            buttons_layout.addWidget(button, row, column, 1, 2)  # Span 2 columns
                        else:
                            buttons_layout.addWidget(button, row, column)
                elif column == 3:
                    button = QPushButton(self.signs[row])
                    button.clicked.connect(self.button_clicked)
                    buttons_layout.addWidget(button, row, column)
                else:
                    button = QPushButton(str(counter))
                    button.clicked.connect(self.button_clicked)
                    buttons_layout.addWidget(button, row, column)
                    counter += 1
            if not row == 0 and not row == 4:
                counter -= 6

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
            self.result_field.setText(str(result))
        else:
            self.result_field.setText("ERROR")

    def restart(self):
        self.result_field.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
