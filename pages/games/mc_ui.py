# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mc.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidgetItem, QSizePolicy, QWidget)

from qfluentwidgets import (ListWidget, Pivot)

class Ui_McDownloadPage(object):
    def setupUi(self, McDownloadPage):
        if not McDownloadPage.objectName():
            McDownloadPage.setObjectName(u"McDownloadPage")
        McDownloadPage.resize(549, 433)
        self.ListWidget = ListWidget(McDownloadPage)
        self.ListWidget.setObjectName(u"ListWidget")
        self.ListWidget.setGeometry(QRect(10, 70, 531, 321))
        self.Pivot = Pivot(McDownloadPage)
        self.Pivot.setObjectName(u"Pivot")
        self.Pivot.setGeometry(QRect(10, 10, 219, 47))

        self.retranslateUi(McDownloadPage)

        QMetaObject.connectSlotsByName(McDownloadPage)
    # setupUi

    def retranslateUi(self, McDownloadPage):
        McDownloadPage.setWindowTitle(QCoreApplication.translate("McDownloadPage", u"Download", None))
    # retranslateUi

