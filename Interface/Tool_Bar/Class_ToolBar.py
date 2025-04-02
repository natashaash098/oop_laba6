from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QToolBar, QPushButton

from Interface.Tool_Bar.Class_PushButton import PushButton


class ToolBar(QToolBar):
    circleSelected = pyqtSignal(str)
    squareSelected = pyqtSignal(str)
    triangleSelected = pyqtSignal(str)
    lineSelected = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.__btn_circle = PushButton()
        self.__btn_square = PushButton()
        self.__btn_triangle = PushButton()
        self.__btn_line = PushButton()

        self.__initUI()
        self.__initSignalsTracking()

    def __selectCircle(self):
        self.__btn_circle.activate()
        self.__btn_square.deactivate()
        self.__btn_triangle.deactivate()
        self.__btn_line.deactivate()

        self.circleSelected.emit("")

    def __selectSquare(self):
        self.__btn_circle.deactivate()
        self.__btn_square.activate()
        self.__btn_triangle.deactivate()
        self.__btn_line.deactivate()

        self.squareSelected.emit("")

    def __selectTriangle(self):
        self.__btn_circle.deactivate()
        self.__btn_square.deactivate()
        self.__btn_triangle.activate()
        self.__btn_line.deactivate()

        self.triangleSelected.emit("")

    def __selectLine(self):
        self.__btn_circle.deactivate()
        self.__btn_square.deactivate()
        self.__btn_triangle.deactivate()
        self.__btn_line.activate()

        self.lineSelected.emit("")

    def __initUI(self):
        self.setMovable(False)

        self.addWidget(self.__btn_circle)
        self.addWidget(self.__btn_square)
        self.addWidget(self.__btn_triangle)
        self.addWidget(self.__btn_line)
        self.__btn_square.setText('Square')
        self.__btn_line.setText('Line')
        self.__btn_circle.setText('Circle')
        self.__btn_triangle.setText('Triangle')


    def __initSignalsTracking(self):
        self.__btn_circle.clicked.connect(self.__selectCircle)
        self.__btn_square.clicked.connect(self.__selectSquare)
        self.__btn_triangle.clicked.connect(self.__selectTriangle)
        self.__btn_line.clicked.connect(self.__selectLine)
