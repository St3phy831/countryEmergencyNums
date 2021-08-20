# Project on Emergency Numbers GUI

# Created By Stephanie Hernandez on 07/01/21

# Description: This GUI outputs the emergency numbers of a specific country, which is
# specified by a person's selection of country and type of emergency. This GUI uses
# the EmergencyAPI to display a country's emergency numbers.
# Documentation for EmergencyAPI: https://github.com/BalestraPatrick/EmergencyAPI

import sys
import requests, json
from choices import codes, choices
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLineEdit,
                               QVBoxLayout, QComboBox)

def get_emergency_num(country_text, emergency_text):
    """
    Returns a country's specific type of emergency number.
    """
    # Since Cyprus and Northern Cyprus have same code, it ouputs Cyprus' emergency
    # numbers instead of Northern Cyprus, so I added if statements to output correct
    #  info for Northern Cyprus.
    if country_text == "Northern Cyprus":
        if emergency_text == "Fire":
            return 199
        elif emergency_text == "Police":
            return 115
        else:
            return 112

    code = codes[country_text]
    endpoint = 'http://emergency-phone-numbers.herokuapp.com/country/' + code

    try:
        # Get request
        r = requests.get(endpoint)
        data = r.json()
    except:
        print('please try again\n\n')

    if data:
        # Since the API returns a dictionary type object for a specific country, I use
        # the data object and key of either "fire", "police", or "medical" to access
        # and return the phone number. 
        return data[emergency_text.lower()]
    else:
        print('no data\n\n')

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

        # Instantiates popup list of coutries
        self.countries = QComboBox()
        self.countries.addItems(self.country_list)

        # Instantiates popup list of types of emergency numbers
        self.emergency_type = QComboBox()
        self.emergency_type.addItems(self.emergency_list)

        self.my_label = QLabel("")

        vbox = QVBoxLayout()
        # Adds elements to vertical layout
        vbox.addWidget(self.title)
        vbox.addWidget(self.countries)
        vbox.addWidget(self.emergency_type)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_label)

        # Sets up a vertical layout
        self.setLayout(vbox)

    @Slot()
    def update_ui(self):
        """
        Displays a country's specific type of emergency number.
        """
        country_text = self.countries.currentText()
        emergency_text = self.emergency_type.currentText()
        emergency_num = get_emergency_num(country_text, emergency_text)
        self.my_label.setText(f'{country_text}\'s {emergency_text} Phone Number:\n\n{emergency_num}')


app = QApplication([])
# create an instance of MyWindow
my_win = MyWindow()
my_win.show()
# app.exec_() runs the main loop
# putting it in sys.exit() allows for a graceful exit
sys.exit(app.exec())