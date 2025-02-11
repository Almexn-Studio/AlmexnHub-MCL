from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QListWidgetItem

from qfluentwidgets import BodyLabel, Dialog
import os
import json
import requests
from .mc_ui import Ui_McDownloadPage

class McDownloadPage(QWidget, Ui_McDownloadPage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        mc_lists = requests.get('https://bmclapi2.bangbang93.com/mc/game/version_manifest.json')
       
        self.Pivot.addItem(routeKey='release', text='正式版')
        self.Pivot.addItem(routeKey='snapshot', text='快照版')

        self.Pivot.setCurrentItem('release')

        data = mc_lists.json()
        # 提取 versions 字段
        versions = data.get("versions", [])

        # 筛选 type 数据
        game_versions = [v for v in versions if v.get("type") == 'release']
        #game_versions = [v for v in versions if v.get("type") == 'snapshot']

        # 渲染到列表
        for item in game_versions:
            list_item = QListWidgetItem()
            # 设置显示内容（name 和 date）
            name = item.get("id", "Unknown")
            date = item.get("releaseTime", "Unknown Date")
            list_item.setText(f"{name} - {date}")

                # 添加到列表
            self.ListWidget.addItem(list_item)
        
