from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QPolygonF

from Figures.Class_Figure import Figure


class Triangle(Figure):
    def __init__(self, x: float, y: float, canvas):
        super().__init__(x, y, canvas)
        self._adjustCoord()

        self.__triangle = QPolygonF()
        self.__createTriangle()
    def __createTriangle(self):
        point_1 = QPointF(self._x + self._width / 2, self._y)
        point_2 = QPointF(self._x, self._y + self._height)
        point_3 = QPointF(self._x + + self._width, self._y + self._height)

        self.__triangle = QPolygonF([point_1, point_2, point_3])
    def draw(self, painter):
        if self._is_selected:
            painter.setPen(self._pen_selected)
            painter.setBrush(self._brush_selected)
        else:
            painter.setPen(self._pen_figure)
            painter.setBrush(self._brush_figure)
        painter.drawConvexPolygon(self.__triangle)

    def increase(self, increase_number: float):
        super().increase(increase_number)
        self.__createTriangle()
    def decrease(self, increase_number: float):
        super().decrease(increase_number)
        self.__createTriangle()

    def moveUp(self, move_distance: float):
        res = super().moveUp(move_distance)
        self.__createTriangle()
        return res
    def moveDown(self, move_distance: float):
        res = super().moveDown(move_distance)
        self.__createTriangle()
        return res
    def moveLeft(self, move_distance: float):
        res = super().moveLeft(move_distance)
        self.__createTriangle()
        return res
    def moveRight(self, move_distance: float):
        res = super().moveRight(move_distance)
        self.__createTriangle()
        return res
    def containsPoint(self, pos: QPointF):
        return self.__triangle.containsPoint(pos, Qt.FillRule.OddEvenFill)