# Project on Emergency Numbers GUI

# Created By Stephanie Hernandez on 07/01/21

# Description: This GUI outputs the emergency numbers of a specific country, which is
# specified by a person's selection of country and type of emergency. This GUI uses
# the EmergencyAPI to display a country's emergency numbers.
# Documentation for EmergencyAPI: https://github.com/BalestraPatrick/EmergencyAPI

import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLineEdit,
                               QVBoxLayout, QComboBox)
from PySide6.QtCore import Slot, Qt
from choices import codes, choices

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Emergency Numbers')
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

        self.country_list = choices
        self.emergency_list = ["Police", "Medical", "Fire"]

        self.title = QLabel("Find a Country's Emergency Number:")

        self.my_btn = QPushButton("Enter")
        self.my_btn.clicked.connect(self.update_ui)

        self.countries = QComboBox()
        self.countries.addItems(self.country_list)

        self.emergency_type = QComboBox()
        self.emergency_type.addItems(self.emergency_list)

        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addWidget(self.countries)
        vbox.addWidget(self.emergency_type)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_label)

        self.setLayout(vbox)

    @Slot()
    def update_ui(self):
        country_text = self.countries.currentText()
        emergency_text = self.emergency_type.currentText()
        # For now, it's 911 until I make a function with the logic to retrieve the
        # country's specific emergency phone number through an endpoint.
        self.my_label.setText(f'{country_text}\'s {emergency_text} Phone Number:\n\n911')


app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(app.exec())