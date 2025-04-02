from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPushButton, QColorDialog

class ColorPanel(QPushButton):
    colorChanged = pyqtSignal(str)

    def __init__(self, w: int, h: int):
        super().__init__()
        self.__color = QColor(0, 0, 0)
        self.__initUI(w, h)
        self.__initSignalsTracking()
    def changeColorColorPanel(self, color: QColor):
        self.__color = color
        r = color.red()
        g = color.green()
        b = color.blue()
        self.setStyleSheet(
            f"""
                border-radius: 25px;
                border: 1px solid rgb(0, 0, 0);
                background-color: rgb({r}, {g}, {b});
                color: rgb({255 - r}, {255 - g}, {255 - b});
                font: 12pt;
            """
        )
    def changeColor(self, color: QColor):
        self.__color = color
        self.colorChanged.emit("")
    def chooseColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.changeColor(color)
    def getColor(self):
        return self.__color
    def __initUI(self, w: int, h: int):
        self.setFixedSize(w, h)
        self.setText("Цвет фигуры")

    def __initSignalsTracking(self):
        self.clicked.connect(self.chooseColor)
