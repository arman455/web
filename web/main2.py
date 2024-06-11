import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QLineEdit, QMessageBox

app = QApplication([])

win = QWidget()
win.show()

val1 = QLineEdit()
val2 = QLineEdit()
amount = QLineEdit()
button = QPushButton()

vertical = QVBoxLayout()
vertical.addWidget(val1)
vertical.addWidget(val2)
vertical.addWidget(amount)
vertical.addWidget(button)

win.setLayout(vertical)

def http_func():
    url = f"https://api.apilayer.com/exchangerates_data/convert?from={val1.text()}&to={val2.text()}&amount={amount.text()}"
    headers = {
        "apikey" : "TOKEN_HERE"
    }
    result = requests.get(url = url, headers = headers)
    print(result.json())

button.clicked.connect(http_func)

app.exec()