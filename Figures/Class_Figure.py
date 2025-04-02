from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QBrush, QColor, QPen

class Figure:
    def __init__(self, x: float, y: float, canvas):
        self._width = 100
        self._height = 100

        self._canvas = canvas

        self._x = x
        self._y = y

        self._is_selected = False
        self._brush_selected = QBrush(QColor(166, 227, 233, 0))
        self._pen_selected = QPen(QColor(227, 74, 141, 150), 10)
        self._brush_figure = QBrush(canvas.getFigureModel().getColorFigure())
        self._pen_figure = QPen(QColor(0, 0, 0), 2)

    def isSelected(self):
        return self._is_selected
    def select(self):
        self._is_selected = True
    def unselect(self):
        self._is_selected = False
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height

    def changeColor(self, color: QColor):
        self._brush_figure = QBrush(color)

    def increase(self, increase_number: float):
        self._width += increase_number
        self._height += increase_number
    def decrease(self, decrease_number: float):
        self._width -= decrease_number
        self._height -= decrease_number

    def moveUp(self, move_distance: float):
        self._y -= move_distance
        return self._adjustCoord()
    def moveDown(self, move_distance: float):
        self._y += move_distance
        return self._adjustCoord()
    def moveRight(self, move_distance: float):
        self._x += move_distance
        return self._adjustCoord()
    def moveLeft(self, move_distance: float):
        self._x -= move_distance
        return self._adjustCoord()

    def getMinX(self):
        return self._x - self._pen_figure.width() / 2
    def getMaxX(self):
        return self._x + self._width + self._pen_figure.width() / 2
    def getMinY(self):
        return self._y - self._pen_figure.width() / 2
    def getMaxY(self):
        return self._y + self._height + self._pen_figure.width() / 2

    def draw(self, painter):
        pass
    def containsPoint(self, pos: QPointF):
        pass

    def _adjustCoord(self):
        adjust_distance = 0
        if self._x + self._width + self._pen_figure.width() / 2 > self._canvas.size().width():
            adjust_distance = self._x - (self._canvas.size().width() - self._width - self._pen_figure.width() / 2)
            self._x = self._canvas.size().width() - self._width - self._pen_figure.width() / 2
        if self._x - self._pen_figure.width() / 2 < 0:
            adjust_distance = self._pen_figure.width() / 2 - self._x
            self._x = self._pen_figure.width() / 2

        if self._y + self._height + self._pen_figure.width() / 2 > self._canvas.size().height():
            adjust_distance = self._y - (self._canvas.size().height() - self._height - self._pen_figure.width() / 2)
            self._y = self._canvas.size().height() - self._height - self._pen_figure.width() / 2
        if self._y - self._pen_figure.width() / 2 < 0:
            adjust_distance = self._pen_figure.width() / 2 - self._y
            self._y = self._pen_figure.width() / 2
        return adjust_distance