from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class UiBridge:
    def __init__(self,mainwindow):
        self.window = mainwindow

    def change_theme(self,theme):
        if theme.lower == "dark":
            QApplication.styleHints().setColorScheme(Qt.ColorScheme.Dark)
        elif theme.lower() == "light":
            QApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
        else:
            QApplication.styleHints().unsetColorScheme()
