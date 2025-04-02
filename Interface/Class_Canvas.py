from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtWidgets import QLabel

from Models.Class_Figure_Model import FiguresModel


class Canvas(QLabel):
    colorFigureChanged = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.__canvas_base = QPixmap(842, 595)
        self.__painter = QPainter(self.__canvas_base)

        self.__initUI()

        self.__figure_model = FiguresModel(self)

        self.__initSignalsTracking()

    def __initUI(self):
        self.__canvas_base.fill(QColor(121, 121, 121))
        self.setPixmap(self.__canvas_base)
        self.setFixedSize(842, 595)
        self.setStyleSheet(
            """
                background-color: rgb(0, 0, 0);
            """
        )
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def repaintFigure(self):
        self.__canvas_base.fill(QColor(248, 253, 241))
        for figure in self.__figure_model.getContainer():
            figure.draw(self.__painter)
        self.setPixmap(self.__canvas_base)
    def changeColorFigure(self):
        self.repaintFigure()
        self.colorFigureChanged.emit("")
    def getCanvasBase(self):
        return self.__canvas_base
    def getFigureModel(self):
        return self.__figure_model
    def mousePressEvent(self, ev):
        if not ev.button() == Qt.MouseButton.LeftButton:
            return None
        pos = ev.position()
        self.__figure_model.mousePressEventHandler(pos)
    def __initSignalsTracking(self):
        self.__figure_model.selectFiguresSizeChanged.connect(self.repaintFigure)

        self.__figure_model.selectFiguresMoved.connect(self.repaintFigure)

        self.__figure_model.selectFiguresDeleted.connect(self.repaintFigure)

        self.__figure_model.figureAdded.connect(self.repaintFigure)

        self.__figure_model.figureSelected.connect(self.repaintFigure)

        self.__figure_model.colorFigureChanged.connect(self.changeColorFigure)
