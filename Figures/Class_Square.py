from PyQt6.QtCore import QPoint, QRectF, QPointF
from PyQt6.QtGui import QPen, QBrush, QColor

from Figures.Class_Figure import Figure

class Square(Figure):
    def __init__(self, x: float, y: float, canvas):
        super().__init__(x, y, canvas)
        self._adjustCoord()

    def draw(self, painter):
        if self._is_selected:
            painter.setBrush(self._brush_selected)
            painter.setPen(self._pen_selected)
        else:
            painter.setBrush(self._brush_figure)
            painter.setPen(self._pen_figure)
        painter.drawRect(QRectF(self._x, self._y, self._width, self._height))
    def containsPoint(self, pos: QPointF):
        x = pos.x()
        y = pos.y()

        return (x >= self._x) and (x <= (self._x + self._width)) and (y >= self._y) and (
                y <= self._y + self._height)