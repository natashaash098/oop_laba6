from PyQt6.QtCore import pyqtSignal, QObject, QPointF
from PyQt6.QtGui import QColor
from Figures.Class_Circle import Circle
from Figures.Class_Line import Line
from Figures.Class_Square import Square
from Figures.Class_Triangle import Triangle

class FiguresModel(QObject):
    colorFigureChanged = pyqtSignal(str)
    figureAdded = pyqtSignal(str)
    figureSelected = pyqtSignal(str)
    selectFiguresDeleted = pyqtSignal(str)
    selectFiguresMoved = pyqtSignal(str)
    selectFiguresSizeChanged = pyqtSignal(str)

    def __init__(self, canvas):
        super().__init__()
        self.__color_figure = QColor(113, 201, 206)
        self.__minimum_rgb = 0
        self.__maximum_rgb = 255
        self.__current_figure = ""
        self.__available_figures = ["Circle", "Square", "Triangle", "Line"]
        self.__select_all = False
        self.__select_several = False
        self.__move_distance = 10
        self.__resizing_number = 5
        self.__container = []
        self.__canvas = canvas

    def increaseSizeSelectedFigure(self):
        flag = True
        for figure in self.__container:
            if figure.isSelected():
                if figure.getMaxX() + self.__resizing_number <= self.__canvas.size().width() \
                        and \
                        figure.getMaxY() + self.__resizing_number <= self.__canvas.size().height():
                    continue
                flag = False
                break

        if flag:
            for figure in self.__container:
                if figure.isSelected():
                    if figure.getMaxX() + self.__resizing_number <= self.__canvas.size().width() \
                            and \
                            figure.getMaxY() + self.__resizing_number <= self.__canvas.size().height():
                        figure.increase(self.__resizing_number)
            self.selectFiguresSizeChanged.emit("")

    def decreaseSizeSelectedFigure(self):
        flag = True
        for figure in self.__container:
            if figure.isSelected():
                if figure.getWidth() - self.__resizing_number >= 50 \
                        and \
                        figure.getHeight() - self.__resizing_number >= 50:
                    continue
                flag = False
                break

        if flag:
            for figure in self.__container:
                if figure.isSelected():
                    if figure.getWidth() - self.__resizing_number >= 50 \
                            and \
                            figure.getHeight() - self.__resizing_number >= 50:
                        figure.decrease(self.__resizing_number)
            self.selectFiguresSizeChanged.emit("")

    def moveUpSelectedFigure(self):
        min_y = self.__canvas.size().height()
        index = 0

        for figure in self.__container:
            if figure.isSelected():
                y = figure.getMinY()
                if y < min_y:
                    min_y = y
                    index = self.__container.index(figure)

        if min_y > 0:
            move_distance = self.__move_distance - self.__container[index].moveUp(self.__move_distance)
            for figure in self.__container:
                if self.__container.index(figure) == index:
                    continue
                if figure.isSelected():
                    figure.moveUp(move_distance)
            self.selectFiguresMoved.emit("")

    def moveDownSelectedFigure(self):
        max_y = 0
        index = 0

        for figure in self.__container:
            if figure.isSelected():
                y = figure.getMaxY()
                if y > max_y:
                    max_y = y
                    index = self.__container.index(figure)

        if max_y < self.__canvas.size().height():
            move_distance = self.__move_distance - self.__container[index].moveDown(self.__move_distance)
            for figure in self.__container:
                if self.__container.index(figure) == index:
                    continue
                if figure.isSelected():
                    figure.moveDown(move_distance)
            self.selectFiguresMoved.emit("")

    def moveLeftSelectedFigure(self):
        min_x = self.__canvas.size().width()
        index = 0

        for figure in self.__container:
            if figure.isSelected():
                x = figure.getMinX()
                if x < min_x:
                    min_x = x
                    index = self.__container.index(figure)

        if min_x > 0:
            move_distance = self.__move_distance - self.__container[index].moveLeft(self.__move_distance)
            for figure in self.__container:
                if self.__container.index(figure) == index:
                    continue
                if figure.isSelected():
                    figure.moveLeft(move_distance)
            self.selectFiguresMoved.emit("")

    def moveRightSelectedFigure(self):
        max_x = 0
        index = 0

        for figure in self.__container:
            if figure.isSelected():
                x = figure.getMaxX()
                if x > max_x:
                    max_x = x
                    index = self.__container.index(figure)

        if max_x < self.__canvas.size().width():
            move_distance = self.__move_distance - self.__container[index].moveRight(self.__move_distance)
            for figure in self.__container:
                if self.__container.index(figure) == index:
                    continue
                if figure.isSelected():
                    figure.moveRight(move_distance)
            self.selectFiguresMoved.emit("")

    def deleteSelectedFigure(self):
        new_container = []
        for figure in self.__container:
            if figure.isSelected():
                continue
            new_container.append(figure)
        self.__container = new_container

        if self.__container:
            self.__container[-1].select()

        self.selectFiguresDeleted.emit("")

    def mousePressEventHandler(self, pos: QPointF):
        flag = True

        if not self.__select_several:
            for figure in self.__container:
                figure.unselect()

        for i in range(len(self.__container) - 1, -1, -1):
            figure = self.__container[i]
            if figure.containsPoint(pos):
                flag = False
                figure.select()
                if not self.__select_all:
                    break

        if flag:
            for figure in self.__container:
                figure.unselect()

            match self.__current_figure:
                case "Circle":
                    figure = Circle(pos.x(), pos.y(), self.__canvas)
                case "Square":
                    figure = Square(pos.x(), pos.y(), self.__canvas)
                case "Triangle":
                    figure = Triangle(pos.x(), pos.y(), self.__canvas)
                case "Line":
                    figure = Line(pos.x(), pos.y(), self.__canvas)
                case _:
                    return None

            figure.select()
            self.__container.append(figure)
            self.figureAdded.emit("")
            return None
        self.figureSelected.emit("")

    def selectCircle(self):
        self.__current_figure = "Circle"

    def selectSquare(self):
        self.__current_figure = "Square"

    def selectTriangle(self):
        self.__current_figure = "Triangle"

    def selectLine(self):
        self.__current_figure = "Line"

    def changeColor(self, color):
        self.__color_figure = color
        self.colorFigureChanged.emit("")

    def setSelectSeveralProperty(self, select_several: bool):
        self.__select_several = select_several

    def setSelectAllProperty(self, select_all: bool):
        self.__select_all = select_all

    def getColorFigure(self):
        return self.__color_figure

    def getContainer(self):
        return self.__container
