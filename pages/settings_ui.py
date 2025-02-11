# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from qfluentwidgets import (Pivot, TitleLabel)

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(549, 433)
        self.Pivot = Pivot(SettingsPage)
        self.Pivot.setObjectName(u"Pivot")
        self.Pivot.setGeometry(QRect(0, 40, 261, 47))
        self.titleLabel = TitleLabel(SettingsPage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(10, 0, 191, 41))

        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)
    # setupUi

    def retranslateUi(self, SettingsPage):
        SettingsPage.setWindowTitle(QCoreApplication.translate("SettingsPage", u"\u8bbe\u7f6e", None))
        self.titleLabel.setText(QCoreApplication.translate("SettingsPage", u"Lancher\u8bbe\u7f6e", None))
    # retranslateUi

