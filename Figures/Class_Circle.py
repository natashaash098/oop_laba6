from PyQt6.QtCore import QPoint, QPointF
from PyQt6.QtGui import QColor, QBrush, QPen

from Figures.Class_Figure import Figure


class Circle(Figure):
    def __init__(self, x: float, y: float, canvas):
        super().__init__(x, y, canvas)
        self._adjustCoord()

        self.__rx = self._width / 2
        self.__ry = self.__rx
    def increase(self, increase_number: float):
        super().increase(increase_number)
        self.__rx = self._width / 2
        self.__ry = self.__rx

    def decrease(self, increase_number: float):
        super().decrease(increase_number)
        self.__rx = self._width / 2
        self.__ry = self.__rx
    def draw(self, painter):
        center = QPointF(self._x + self.__rx, self._y + self.__ry)
        if self._is_selected:
            painter.setBrush(self._brush_selected)
            painter.setPen(self._pen_selected)
        else:
            painter.setBrush(self._brush_figure)
            painter.setPen(self._pen_figure)
        painter.drawEllipse(center, self.__rx, self.__ry)
    def containsPoint(self, pos: QPointF):
        x = pos.x()
        y = pos.y()
        return (self._x + self.__rx - x) ** 2 / self.__rx ** 2 + (self._y + self.__ry - y) ** 2 / self.__ry ** 2 <= 1
