# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novosPoderes.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(473, 498)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"logo_fibra.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(Form)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(0, 0))
        self.frame_logo.setMaximumSize(QSize(16777215, 50))
        self.frame_logo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_logo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_logo)

        self.frame_prennchimento = QFrame(Form)
        self.frame_prennchimento.setObjectName(u"frame_prennchimento")
        self.frame_prennchimento.setFrameShape(QFrame.StyledPanel)
        self.frame_prennchimento.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_prennchimento)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gPBox_cnpj = QGroupBox(self.frame_prennchimento)
        self.gPBox_cnpj.setObjectName(u"gPBox_cnpj")
        font = QFont()
        font.setPointSize(12)
        self.gPBox_cnpj.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.gPBox_cnpj)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lnEdit_cnpj = QLineEdit(self.gPBox_cnpj)
        self.lnEdit_cnpj.setObjectName(u"lnEdit_cnpj")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnEdit_cnpj.sizePolicy().hasHeightForWidth())
        self.lnEdit_cnpj.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.lnEdit_cnpj)


        self.gridLayout.addWidget(self.gPBox_cnpj, 0, 0, 1, 1)

        self.gPBox_emp = QGroupBox(self.frame_prennchimento)
        self.gPBox_emp.setObjectName(u"gPBox_emp")
        self.gPBox_emp.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.gPBox_emp)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lnEdit_emp = QLineEdit(self.gPBox_emp)
        self.lnEdit_emp.setObjectName(u"lnEdit_emp")
        sizePolicy.setHeightForWidth(self.lnEdit_emp.sizePolicy().hasHeightForWidth())
        self.lnEdit_emp.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.lnEdit_emp)


        self.gridLayout.addWidget(self.gPBox_emp, 1, 0, 1, 1)

        self.gPBox_repLeg = QGroupBox(self.frame_prennchimento)
        self.gPBox_repLeg.setObjectName(u"gPBox_repLeg")
        self.gPBox_repLeg.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.gPBox_repLeg)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lnEdit_repLeg = QLineEdit(self.gPBox_repLeg)
        self.lnEdit_repLeg.setObjectName(u"lnEdit_repLeg")
        sizePolicy.setHeightForWidth(self.lnEdit_repLeg.sizePolicy().hasHeightForWidth())
        self.lnEdit_repLeg.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lnEdit_repLeg)


        self.gridLayout.addWidget(self.gPBox_repLeg, 2, 0, 1, 1)

        self.gPBox_email = QGroupBox(self.frame_prennchimento)
        self.gPBox_email.setObjectName(u"gPBox_email")
        self.gPBox_email.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.gPBox_email)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lnEdit_email = QLineEdit(self.gPBox_email)
        self.lnEdit_email.setObjectName(u"lnEdit_email")
        sizePolicy.setHeightForWidth(self.lnEdit_email.sizePolicy().hasHeightForWidth())
        self.lnEdit_email.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.lnEdit_email)


        self.gridLayout.addWidget(self.gPBox_email, 3, 0, 1, 1)

        self.gPBox_venc = QGroupBox(self.frame_prennchimento)
        self.gPBox_venc.setObjectName(u"gPBox_venc")
        self.gPBox_venc.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.gPBox_venc)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.calendarWidget = QCalendarWidget(self.gPBox_venc)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.calendarWidget)


        self.gridLayout.addWidget(self.gPBox_venc, 4, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.frame_prennchimento)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cBox_tpAss = QComboBox(self.groupBox_6)
        self.cBox_tpAss.addItem("")
        self.cBox_tpAss.addItem("")
        self.cBox_tpAss.addItem("")
        self.cBox_tpAss.addItem("")
        self.cBox_tpAss.setObjectName(u"cBox_tpAss")
        sizePolicy.setHeightForWidth(self.cBox_tpAss.sizePolicy().hasHeightForWidth())
        self.cBox_tpAss.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.cBox_tpAss)


        self.gridLayout.addWidget(self.groupBox_6, 5, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_prennchimento)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pButton_salvar = QPushButton(self.frame)
        self.pButton_salvar.setObjectName(u"pButton_salvar")
        self.pButton_salvar.setMinimumSize(QSize(0, 25))
        self.pButton_salvar.setMaximumSize(QSize(16777215, 25))
        self.pButton_salvar.setFont(font)

        self.verticalLayout_9.addWidget(self.pButton_salvar)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gPBox_cnpj.setTitle(QCoreApplication.translate("Form", u"CNPJ:", None))
        self.gPBox_emp.setTitle(QCoreApplication.translate("Form", u"EMPRESA:", None))
        self.gPBox_repLeg.setTitle(QCoreApplication.translate("Form", u"REPRESENTANTE LEGAL:", None))
        self.gPBox_email.setTitle(QCoreApplication.translate("Form", u"EMAIL:", None))
        self.gPBox_venc.setTitle(QCoreApplication.translate("Form", u"VENCIMENTO:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"TIPO DE ASSINATURA:", None))
        self.cBox_tpAss.setItemText(0, QCoreApplication.translate("Form", u"AVALISTA", None))
        self.cBox_tpAss.setItemText(1, QCoreApplication.translate("Form", u"FIADOR", None))
        self.cBox_tpAss.setItemText(2, QCoreApplication.translate("Form", u"FIEL DEPOSIT\u00c1RIO", None))
        self.cBox_tpAss.setItemText(3, QCoreApplication.translate("Form", u"PARTE", None))

        self.cBox_tpAss.setCurrentText(QCoreApplication.translate("Form", u"AVALISTA", None))
        self.pButton_salvar.setText(QCoreApplication.translate("Form", u"SALVAR", None))
    # retranslateUi

