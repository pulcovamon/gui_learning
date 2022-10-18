import sys                  # for allowing app's termination and exit status through the exit() function
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])      # create instance

# create gui
window = QWidget()
window.setWindowTitle('PyQt App')
window.setGeometry(100, 100, 280, 80)
hello_msg = QLabel('<h1>Hello, World</h1>', parent = window)
hello_msg.move(60, 15)