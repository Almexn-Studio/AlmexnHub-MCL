from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout

from qfluentwidgets import BodyLabel
from .netgame_ui import Ui_NetGamePage

class NetGamePage(QWidget, Ui_NetGamePage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)