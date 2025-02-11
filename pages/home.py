from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout

from qfluentwidgets import BodyLabel, Dialog
import os
from .home_ui import Ui_HomePage

class HomePage(QWidget, Ui_HomePage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.HeaderCardWidget.infoLabel = BodyLabel('测试公告')
        self.gg_hBoxLayout = QHBoxLayout()
        self.gg_hBoxLayout.addWidget(self.HeaderCardWidget.infoLabel)
        self.HeaderCardWidget.viewLayout.addLayout(self.gg_hBoxLayout)

        #??JAVA??
        jdk_path = os.getenv('JAVA_HOME')
        if jdk_path != None:
            self.Dialog('环境异常','无法在环境中找到 JAVA_HOME ,请检查配置是否正确，或前往[设置]页下载多版本JAVA', window)