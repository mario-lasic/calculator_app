from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit, QLabel,
                               QGridLayout,)
import sys
from calculate import Calculate

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        self.createUI()
        self.apply_style()

    # This method will create the UI of the calculator
    def createUI(self):
        self.result_field = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.result_field)

        self.signs = [['AC', '^', '%', '/'], ['7', '8', '9', 'X'], 
                      ['4', '5', '6', '-'], ['1', '2', '3', '+'], 
                      ['0', '.', '=', '']]
        
        # Create the buttons
        buttons_layout = QGridLayout()
        for row in range(5):
            for column in range(4):
                if self.signs[row][column] == '':
                    continue
                button = QPushButton(self.signs[row][column])
                button.clicked.connect(self.button_clicked)
                if row == 4 and column == 2:
                    button.setObjectName('equals')
                    buttons_layout.addWidget(button, row, column, 1, 2)  # Span 2 columns
                else:
                    buttons_layout.addWidget(button, row, column)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    # This method will apply the style to the calculator
    def apply_style(self):
        with open ('style.qss', 'r') as file:
            style = file.read()
            self.setStyleSheet(style)

    # This method will handle the button click event
    def button_clicked(self):
        button = self.sender()
        value = button.text()
        if value == 'AC':
            self.restart()
        elif value == '=':
            calculate = Calculate(self.result_field.text())
            result = calculate.calculate()
            self.result_field.setText(str(result))
        else:
            self.result_field.setText(self.result_field.text() + value)

    def restart(self):
        self.result_field.setText('')

# This method will run the application
def run():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
