from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QCheckBox, QWidget, QGridLayout, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QHBoxLayout, QToolBar, QButtonGroup, QPushButton
from Interface.Class_Canvas import Canvas
from Interface.Color_Panel.Class_Color_Panel import ColorPanel
from Interface.Tool_Bar.Class_ToolBar import ToolBar



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__canvas = Canvas()

        self.__color_panel = ColorPanel(100, 50)
        self.__tool_bar = ToolBar()

        self.__check_box_select_all = QCheckBox()

        self.__initUI()
        self.__initSignalsTracking()



    def __initUI(self):
        center_widget = QWidget()
        self.setCentralWidget(center_widget)
        self.setStyleSheet(
            """
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                font: 14pt;
            """
        )


        self.addToolBar(self.__tool_bar)
        self.setGeometry(200, 60, 1024, 707)

        self.__check_box_select_all.setFixedSize(110, 50)
        self.__check_box_select_all.setText("Select All")

        canvas_field = QWidget()
        canvas_field.setStyleSheet(
            """
                background-color: rgb(227,241,208);
            """
        )
        grid_layout = QGridLayout(canvas_field)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.addWidget(self.__canvas)

        vertical_widget = QWidget()
        vertical_widget.setFixedWidth(112)
        vertical_widget.setMinimumHeight(470)
        vertical_layout = QVBoxLayout(vertical_widget)
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.addWidget(self.__check_box_select_all)
        vertical_layout.addItem(
            QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding))
        vertical_layout.addWidget(self.__color_panel)

        horizontal_layout = QHBoxLayout(center_widget)
        horizontal_layout.setSpacing(10)
        horizontal_layout.setContentsMargins(20, 20, 20, 20)
        horizontal_layout.addWidget(canvas_field)
        horizontal_layout.addWidget(vertical_widget)

        self.__color_panel.changeColorColorPanel(self.__canvas.getFigureModel().getColorFigure())
        self.__canvas.repaintFigure()

        self.setFocus()
    def __initSignalsTracking(self):
        self.__canvas.colorFigureChanged.connect(
            lambda: self.__color_panel.changeColorColorPanel(self.__canvas.getFigureModel().getColorFigure())
        )

        self.__color_panel.colorChanged.connect(
            lambda: self.__canvas.getFigureModel().changeColor(self.__color_panel.getColor())
        )
        self.__tool_bar.circleSelected.connect(self.__canvas.getFigureModel().selectCircle)
        self.__tool_bar.squareSelected.connect(self.__canvas.getFigureModel().selectSquare)
        self.__tool_bar.triangleSelected.connect(self.__canvas.getFigureModel().selectTriangle)
        self.__tool_bar.lineSelected.connect(self.__canvas.getFigureModel().selectLine)

        self.__check_box_select_all.stateChanged.connect(
            lambda: self.__canvas.getFigureModel().setSelectAllProperty(self.__check_box_select_all.isChecked())
        )

    def keyPressEvent(self, a0):
        print(a0.key())
        self.setFocus()
        if a0.key() == 16777223:
            self.__canvas.getFigureModel().deleteSelectedFigure()

        if a0.key() == 16777249:
            self.__canvas.getFigureModel().setSelectSeveralProperty(True)

        if a0.key() == 16777235:
            self.__canvas.getFigureModel().moveUpSelectedFigure()

        if a0.key() == 16777237:
            self.__canvas.getFigureModel().moveDownSelectedFigure()

        if a0.key() == 16777234:
            self.__canvas.getFigureModel().moveLeftSelectedFigure()

        if a0.key() == 16777236:
            self.__canvas.getFigureModel().moveRightSelectedFigure()

        if a0.modifiers() == Qt.KeyboardModifier.ControlModifier and a0.key() == 61:
            self.__canvas.getFigureModel().increaseSizeSelectedFigure()

        if a0.modifiers() == Qt.KeyboardModifier.ControlModifier and a0.key() == 45:
            self.__canvas.getFigureModel().decreaseSizeSelectedFigure()

    def keyReleaseEvent(self, a0):
        if a0.key() == 16777249:
            self.__canvas.getFigureModel().setSelectSeveralProperty(False)
