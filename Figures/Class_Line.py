import math
from PyQt6.QtCore import QLineF, QPointF, Qt
from PyQt6.QtGui import QPen, QPolygonF

from Figures.Class_Figure import Figure


class Line(Figure):
    def __init__(self, x: float, y: float, canvas):
        super().__init__(x, y, canvas)
        self.__thickness = 5
        self._adjustCoord()

        self.__line = QLineF()
        self.__createLine()
    def __createLine(self):
        point_1 = QPointF(self._x, self._y)
        point_2 = QPointF(self._x + self._width, self._y + self._height)
        self.__line = QLineF(point_1, point_2)

    def increase(self, increase_number: float):
        super().increase(increase_number)
        self.__createLine()
    def decrease(self, decrease_number: float):
        super().increase(decrease_number)
        self.__createLine()

    def moveUp(self, move_distance: float):
        res = super().moveUp(move_distance)
        self.__createLine()
        return res
    def moveDown(self, move_distance: float):
        res = super().moveDown(move_distance)
        self.__createLine()
        return res
    def moveLeft(self, move_distance: float):
        res = super().moveLeft(move_distance)
        self.__createLine()
        return res
    def moveRight(self, move_distance: float):
        res = super().moveRight(move_distance)
        self.__createLine()
        return res
    def draw(self, painter):
        if self._is_selected:
            painter.setBrush(self._brush_selected)
            painter.setPen(QPen(self._pen_selected.color(), self._pen_selected.width() + self.__thickness))
        else:
            painter.setPen(QPen(self._brush_figure.color(), self.__thickness))
        painter.drawLine(self.__line)
    def containsPoint(self, pos: QPointF):
        hip = math.sqrt((self.__thickness / 2) ** 2 + (self.__thickness / 2) ** 2)
        point_1 = QPointF(self._x, self._y - hip)
        point_2 = QPointF(self._x + self._width + hip, self._y + self._height)
        point_3 = QPointF(self._x + self._width, self._y + self._height + hip)
        point_4 = QPointF(self._x - hip, self._y)
        polygon = QPolygonF([point_1, point_2, point_3, point_4])
        return polygon.containsPoint(pos, Qt.FillRule.OddEvenFill)

    def getMinimumY(self):
        hip = math.sqrt((self.__thickness / 2) ** 2 + (self.__thickness / 2) ** 2)
        return self.__line.p1().y() - hip
    def getMaximumY(self):
        hip = math.sqrt((self.__thickness / 2) ** 2 + (self.__thickness / 2) ** 2)
        return self.__line.p2().y() + hip
    def getMinimumX(self):
        hip = math.sqrt((self.__thickness / 2) ** 2 + (self.__thickness / 2) ** 2)
        return self.__line.p1().x() - hip
    def getMaximumX(self):
        hip = math.sqrt((self.__thickness / 2) ** 2 + (self.__thickness / 2) ** 2)
        return self.__line.p2().x() + hip

    def _adjustCoord(self):
        adjust_distance = 0
        hip = math.sqrt((self.__thickness / 2) ** 2 + (self.__thickness / 2) ** 2)
        if self._x + self._width + hip > self._canvas.size().width():
            adjust_distance = self._x - self._canvas.size().width() + self._width + hip
            self._x = self._canvas.size().width() - self._width - hip
        if self._x - hip < 0:
            adjust_distance = hip - self._x
            self._x = hip
        if self._y + self._height + hip > self._canvas.size().height():
            adjust_distance = self._y - (self._canvas.size().height() - self._height - hip)
            self._y = self._canvas.size().height() - self._height - hip
        if self._y - hip < 0:
            adjust_distance = hip - self._y
            self._y = hip
        return adjust_distance
