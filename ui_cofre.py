# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cofre.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 650)
        MainWindow.setMinimumSize(QSize(950, 650))
        icon = QIcon()
        icon.addFile(u"logo_fibra.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionVencendo_em_30_dias = QAction(MainWindow)
        self.actionVencendo_em_30_dias.setObjectName(u"actionVencendo_em_30_dias")
        self.actionVencimento_proximo = QAction(MainWindow)
        self.actionVencimento_proximo.setObjectName(u"actionVencimento_proximo")
        self.actionRelat_rio_Excel = QAction(MainWindow)
        self.actionRelat_rio_Excel.setObjectName(u"actionRelat_rio_Excel")
        self.actionFechar = QAction(MainWindow)
        self.actionFechar.setObjectName(u"actionFechar")
        self.actionIncluir = QAction(MainWindow)
        self.actionIncluir.setObjectName(u"actionIncluir")
        self.actionAlterar = QAction(MainWindow)
        self.actionAlterar.setObjectName(u"actionAlterar")
        self.actionExcluir = QAction(MainWindow)
        self.actionExcluir.setObjectName(u"actionExcluir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_table = QFrame(self.centralwidget)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_table)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.frame_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gPBox_cnpj = QGroupBox(self.tab)
        self.gPBox_cnpj.setObjectName(u"gPBox_cnpj")
        font = QFont()
        font.setPointSize(12)
        self.gPBox_cnpj.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.gPBox_cnpj)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lnEdit_cnpj = QLineEdit(self.gPBox_cnpj)
        self.lnEdit_cnpj.setObjectName(u"lnEdit_cnpj")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnEdit_cnpj.sizePolicy().hasHeightForWidth())
        self.lnEdit_cnpj.setSizePolicy(sizePolicy)
        self.lnEdit_cnpj.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_5.addWidget(self.lnEdit_cnpj)


        self.gridLayout.addWidget(self.gPBox_cnpj, 0, 0, 1, 1)

        self.gPBox_emp = QGroupBox(self.tab)
        self.gPBox_emp.setObjectName(u"gPBox_emp")
        self.gPBox_emp.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.gPBox_emp)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lnEdit_emp = QLineEdit(self.gPBox_emp)
        self.lnEdit_emp.setObjectName(u"lnEdit_emp")
        sizePolicy.setHeightForWidth(self.lnEdit_emp.sizePolicy().hasHeightForWidth())
        self.lnEdit_emp.setSizePolicy(sizePolicy)
        self.lnEdit_emp.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_6.addWidget(self.lnEdit_emp)


        self.gridLayout.addWidget(self.gPBox_emp, 0, 1, 1, 1)

        self.gPBox_repLeg = QGroupBox(self.tab)
        self.gPBox_repLeg.setObjectName(u"gPBox_repLeg")
        self.gPBox_repLeg.setFont(font)
        self.verticalLayout_9 = QVBoxLayout(self.gPBox_repLeg)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lnEdit_repLeg = QLineEdit(self.gPBox_repLeg)
        self.lnEdit_repLeg.setObjectName(u"lnEdit_repLeg")
        sizePolicy.setHeightForWidth(self.lnEdit_repLeg.sizePolicy().hasHeightForWidth())
        self.lnEdit_repLeg.setSizePolicy(sizePolicy)
        self.lnEdit_repLeg.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_9.addWidget(self.lnEdit_repLeg)


        self.gridLayout.addWidget(self.gPBox_repLeg, 1, 0, 1, 1)

        self.gPBox_email = QGroupBox(self.tab)
        self.gPBox_email.setObjectName(u"gPBox_email")
        self.gPBox_email.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(self.gPBox_email)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lnEdit_email = QLineEdit(self.gPBox_email)
        self.lnEdit_email.setObjectName(u"lnEdit_email")
        sizePolicy.setHeightForWidth(self.lnEdit_email.sizePolicy().hasHeightForWidth())
        self.lnEdit_email.setSizePolicy(sizePolicy)
        self.lnEdit_email.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_10.addWidget(self.lnEdit_email)


        self.gridLayout.addWidget(self.gPBox_email, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab)
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
        self.cBox_tpAss.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_8.addWidget(self.cBox_tpAss)


        self.gridLayout.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.gPBox_venc = QGroupBox(self.tab)
        self.gPBox_venc.setObjectName(u"gPBox_venc")
        self.gPBox_venc.setMinimumSize(QSize(0, 0))
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


        self.gridLayout.addWidget(self.gPBox_venc, 3, 0, 1, 2)

        self.pushButton_incluir = QPushButton(self.tab)
        self.pushButton_incluir.setObjectName(u"pushButton_incluir")
        self.pushButton_incluir.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.pushButton_incluir, 4, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.groupBox_acoes = QGroupBox(self.tab_2)
        self.groupBox_acoes.setObjectName(u"groupBox_acoes")
        self.groupBox_acoes.setMinimumSize(QSize(100, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_acoes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_alterar = QPushButton(self.groupBox_acoes)
        self.pushButton_alterar.setObjectName(u"pushButton_alterar")
        self.pushButton_alterar.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.pushButton_alterar)

        self.pushButton_excluir = QPushButton(self.groupBox_acoes)
        self.pushButton_excluir.setObjectName(u"pushButton_excluir")
        self.pushButton_excluir.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.pushButton_excluir)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_excel = QPushButton(self.groupBox_acoes)
        self.pushButton_excel.setObjectName(u"pushButton_excel")
        self.pushButton_excel.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.pushButton_excel)


        self.horizontalLayout_3.addWidget(self.groupBox_acoes)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame_table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 18))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionVencendo_em_30_dias)
        self.menuMenu.addAction(self.actionVencimento_proximo)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionRelat_rio_Excel)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionFechar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionVencendo_em_30_dias.setText(QCoreApplication.translate("MainWindow", u"Vencendo em 30 dias", None))
        self.actionVencimento_proximo.setText(QCoreApplication.translate("MainWindow", u"Vencimento proximo", None))
        self.actionRelat_rio_Excel.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio Excel", None))
        self.actionFechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.actionIncluir.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.actionAlterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.actionExcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.gPBox_cnpj.setTitle(QCoreApplication.translate("MainWindow", u"CNPJ:", None))
        self.gPBox_emp.setTitle(QCoreApplication.translate("MainWindow", u"EMPRESA:", None))
        self.gPBox_repLeg.setTitle(QCoreApplication.translate("MainWindow", u"REPRESENTANTE LEGAL:", None))
        self.gPBox_email.setTitle(QCoreApplication.translate("MainWindow", u"EMAIL:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"TIPO DE ASSINATURA:", None))
        self.cBox_tpAss.setItemText(0, QCoreApplication.translate("MainWindow", u"AVALISTA", None))
        self.cBox_tpAss.setItemText(1, QCoreApplication.translate("MainWindow", u"FIADOR", None))
        self.cBox_tpAss.setItemText(2, QCoreApplication.translate("MainWindow", u"FIEL DEPOSIT\u00c1RIO", None))
        self.cBox_tpAss.setItemText(3, QCoreApplication.translate("MainWindow", u"PARTE", None))

        self.cBox_tpAss.setCurrentText(QCoreApplication.translate("MainWindow", u"AVALISTA", None))
        self.gPBox_venc.setTitle(QCoreApplication.translate("MainWindow", u"VENCIMENTO:", None))
        self.pushButton_incluir.setText(QCoreApplication.translate("MainWindow", u"INCLUIR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"INCLUIR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"EMPRESA", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"REPRESENTANTE LEGAL", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"EMAIL DE CONTATO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"VENCIMENTO MANDATO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TIPO DE ASSINATURA", None));
        self.groupBox_acoes.setTitle(QCoreApplication.translate("MainWindow", u"A\u00c7\u00d5ES:", None))
        self.pushButton_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.pushButton_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.pushButton_excel.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"COFRES", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

