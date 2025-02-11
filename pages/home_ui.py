# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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

from qfluentwidgets import (CardWidget, HeaderCardWidget, SimpleCardWidget)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(549, 433)
        self.HeaderCardWidget = HeaderCardWidget(HomePage)
        self.HeaderCardWidget.setObjectName(u"HeaderCardWidget")
#self.HeaderCardWidget.setGeometry(QRect(10, 10, 221, 211))

        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Home", None))
        self.HeaderCardWidget.setProperty(u"title", QCoreApplication.translate("HomePage", u"\u516c\u544a", None))
    # retranslateUi

