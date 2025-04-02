from PyQt6.QtWidgets import QPushButton

class PushButton(QPushButton):

    def __init__(self):
        super().__init__()

        self.__initUI()
    def activate(self):
        self.setStyleSheet(
            """
                border: none;
                background-color: rgb(159, 226, 191);
            """
        )
    def deactivate(self):
        self.setStyleSheet(
            """
                border: none;
                background-color: rgb(255, 255, 255);
            """
        )

    def __initUI(self):
        self.setFixedSize(100, 60)
        self.setStyleSheet(
            """
                border: none;
            """
        )
        #self.setIcon(icon)
        #self.setIconSize(self.size())
