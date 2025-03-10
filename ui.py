from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLineEdit, QLabel, QGridLayout, QMenuBar)
from PySide6.QtGui import QAction
import sys
from calculate import Calculate

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        self.createUI()
        self.createMenuBar()
        self.apply_style('light')

    def createUI(self):
        self.result_field = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.result_field)

        self.signs = [['AC', '^', '%', '/'], ['7', '8', '9', 'X'], 
                      ['4', '5', '6', '-'], ['1', '2', '3', '+'], 
                      ['0', '.', '=', '']]

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

    def createMenuBar(self):
        menubar = QMenuBar(self)
        style_menu = menubar.addMenu('Style')

        light_action = QAction('Light', self)
        light_action.triggered.connect(lambda: self.apply_style('light'))
        style_menu.addAction(light_action)

        dark_action = QAction('Dark', self)
        dark_action.triggered.connect(lambda: self.apply_style('dark'))
        style_menu.addAction(dark_action)

        layout = self.layout()
        layout.setMenuBar(menubar)

    def apply_style(self, style_name):
        if style_name == 'light':
            with open('light.qss', 'r') as file:
                style = file.read()
        elif style_name == 'dark':
            with open('dark.qss', 'r') as file:
                style = file.read()
        self.setStyleSheet(style)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
