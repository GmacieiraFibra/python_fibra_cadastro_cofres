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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

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
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 100))
        self.frame_header.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_avencer = QFrame(self.frame_header)
        self.frame_avencer.setObjectName(u"frame_avencer")
        self.frame_avencer.setStyleSheet(u"")
        self.frame_avencer.setFrameShape(QFrame.Box)
        self.frame_avencer.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_avencer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_avencer)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.frame_avencer)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.frame_avencer)

        self.frame_vencidos = QFrame(self.frame_header)
        self.frame_vencidos.setObjectName(u"frame_vencidos")
        self.frame_vencidos.setFrameShape(QFrame.Box)
        self.frame_vencidos.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_vencidos)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_vencidos)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame_vencidos)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.frame_vencidos)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_filter = QFrame(self.centralwidget)
        self.frame_filter.setObjectName(u"frame_filter")
        self.frame_filter.setFrameShape(QFrame.StyledPanel)
        self.frame_filter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_filter)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_id = QGroupBox(self.frame_filter)
        self.groupBox_id.setObjectName(u"groupBox_id")
        font = QFont()
        font.setKerning(True)
        self.groupBox_id.setFont(font)
        self.groupBox_id.setFlat(False)
        self.groupBox_id.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_id)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.comboBox_id = QComboBox(self.groupBox_id)
        self.comboBox_id.setObjectName(u"comboBox_id")

        self.horizontalLayout_3.addWidget(self.comboBox_id)


        self.horizontalLayout_8.addWidget(self.groupBox_id)

        self.groupBox_cnpj = QGroupBox(self.frame_filter)
        self.groupBox_cnpj.setObjectName(u"groupBox_cnpj")
        self.groupBox_cnpj.setFlat(False)
        self.groupBox_cnpj.setCheckable(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_cnpj)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.comboBox_cnpj = QComboBox(self.groupBox_cnpj)
        self.comboBox_cnpj.setObjectName(u"comboBox_cnpj")

        self.horizontalLayout_4.addWidget(self.comboBox_cnpj)


        self.horizontalLayout_8.addWidget(self.groupBox_cnpj)

        self.groupBox_emp = QGroupBox(self.frame_filter)
        self.groupBox_emp.setObjectName(u"groupBox_emp")
        self.groupBox_emp.setFlat(False)
        self.groupBox_emp.setCheckable(False)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_emp)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.comboBox_emp = QComboBox(self.groupBox_emp)
        self.comboBox_emp.setObjectName(u"comboBox_emp")

        self.horizontalLayout_5.addWidget(self.comboBox_emp)


        self.horizontalLayout_8.addWidget(self.groupBox_emp)

        self.groupBox_repLeg = QGroupBox(self.frame_filter)
        self.groupBox_repLeg.setObjectName(u"groupBox_repLeg")
        self.groupBox_repLeg.setFlat(False)
        self.groupBox_repLeg.setCheckable(False)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_repLeg)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.comboBox_repLeg = QComboBox(self.groupBox_repLeg)
        self.comboBox_repLeg.setObjectName(u"comboBox_repLeg")

        self.horizontalLayout_6.addWidget(self.comboBox_repLeg)


        self.horizontalLayout_8.addWidget(self.groupBox_repLeg)

        self.pushButton = QPushButton(self.frame_filter)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_filter)

        self.frame_table = QFrame(self.centralwidget)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_table)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(self.frame_table)
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout.addWidget(self.treeWidget)


        self.verticalLayout.addWidget(self.frame_table)

        self.groupBox_acoes = QGroupBox(self.centralwidget)
        self.groupBox_acoes.setObjectName(u"groupBox_acoes")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_acoes)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_incluir = QFrame(self.groupBox_acoes)
        self.frame_incluir.setObjectName(u"frame_incluir")
        self.frame_incluir.setFrameShape(QFrame.StyledPanel)
        self.frame_incluir.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_incluir)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_incluir = QPushButton(self.frame_incluir)
        self.pushButton_incluir.setObjectName(u"pushButton_incluir")
        self.pushButton_incluir.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_9.addWidget(self.pushButton_incluir)


        self.horizontalLayout_7.addWidget(self.frame_incluir)

        self.frame_alterar = QFrame(self.groupBox_acoes)
        self.frame_alterar.setObjectName(u"frame_alterar")
        self.frame_alterar.setFrameShape(QFrame.StyledPanel)
        self.frame_alterar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_alterar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_alterar = QPushButton(self.frame_alterar)
        self.pushButton_alterar.setObjectName(u"pushButton_alterar")
        self.pushButton_alterar.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_11.addWidget(self.pushButton_alterar)


        self.horizontalLayout_7.addWidget(self.frame_alterar)

        self.frame_excluir = QFrame(self.groupBox_acoes)
        self.frame_excluir.setObjectName(u"frame_excluir")
        self.frame_excluir.setFrameShape(QFrame.StyledPanel)
        self.frame_excluir.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_excluir)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_excluir = QPushButton(self.frame_excluir)
        self.pushButton_excluir.setObjectName(u"pushButton_excluir")
        self.pushButton_excluir.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_10.addWidget(self.pushButton_excluir)


        self.horizontalLayout_7.addWidget(self.frame_excluir)


        self.verticalLayout.addWidget(self.groupBox_acoes)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 18))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuA_es = QMenu(self.menubar)
        self.menuA_es.setObjectName(u"menuA_es")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuA_es.menuAction())
        self.menuMenu.addAction(self.actionVencendo_em_30_dias)
        self.menuMenu.addAction(self.actionVencimento_proximo)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionRelat_rio_Excel)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionFechar)
        self.menuA_es.addAction(self.actionIncluir)
        self.menuA_es.addAction(self.actionAlterar)
        self.menuA_es.addAction(self.actionExcluir)

        self.retranslateUi(MainWindow)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dentro do pr\u00f3ximo m\u00eas, haver\u00e1(\u00e3o) \"\" mandato(s) vencendo.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Clique aqui para visualizar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Considerando a data de hoje h\u00e1 \"\" mandato(s) vencido(s)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Clique aqui para visualizar", None))
        self.groupBox_id.setTitle(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.groupBox_cnpj.setTitle(QCoreApplication.translate("MainWindow", u"CNPJ:", None))
        self.groupBox_emp.setTitle(QCoreApplication.translate("MainWindow", u"EMPRESA:", None))
        self.groupBox_repLeg.setTitle(QCoreApplication.translate("MainWindow", u"REPRESENTANTE LEGAL:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"LIMPAR FILTROS", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"TIPO DE ASSINATURA", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"VENCIEMENTO MANDATO", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"EMAIL DE CONTATO", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"REPRESENTANTE LEGAL", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"EMPRESA", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"ID", None));
        self.groupBox_acoes.setTitle(QCoreApplication.translate("MainWindow", u"A\u00c7\u00d5ES:", None))
        self.pushButton_incluir.setText(QCoreApplication.translate("MainWindow", u"INCLUIR", None))
        self.pushButton_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.pushButton_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuA_es.setTitle(QCoreApplication.translate("MainWindow", u"A\u00e7\u00f5es", None))
    # retranslateUi

