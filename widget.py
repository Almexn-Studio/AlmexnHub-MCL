# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout
from PySide6.QtCore import QTimer, QSize, QEventLoop, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from qframelesswindow import FramelessWindow, StandardTitleBar

from qfluentwidgets import FluentWindow, NavigationItemPosition, SubtitleLabel, FluentIcon, setFont
from pages.home import HomePage
from pages.netGame import NetGamePage
from pages.settings import SettingsPage
from pages.games.mcdown import McDownloadPage

class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.resize(900, 600)
        self.setWindowTitle('AlmexnHub-MCL')
        self.setWindowIcon(QIcon('./icon.png'))


        #创建页面
        self.HomePage = HomePage(self)
        self.McDownPage = McDownloadPage(self)
        self.NetGamePage = NetGamePage(self)
        self.SettingsPage = SettingsPage(self)

        self.initNavigation() 
        
    def initNavigation(self):
        self.addSubInterface(self.HomePage, FluentIcon.HOME, '首页')
        self.addSubInterface(self.McDownPage, FluentIcon.DOWNLOAD, '游戏下载')
        self.addSubInterface(self.NetGamePage, FluentIcon.GLOBE, '网络游戏', NavigationItemPosition.SCROLL)
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.SettingsPage, FluentIcon.SETTING, '设置', NavigationItemPosition.BOTTOM)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Window()
    widget.show()
    sys.exit(app.exec())
