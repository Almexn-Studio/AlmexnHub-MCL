from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout

from qfluentwidgets import BodyLabel
from .settings_ui import Ui_SettingsPage

class SettingsPage(QWidget, Ui_SettingsPage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)