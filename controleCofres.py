#Bibliotecas necessárioas
from  PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QMessageBox)
import PySide6.QtCore
from ui_cofre  import Ui_MainWindow
from ui_novosPoderes import Ui_Form
import sys
import getpass
from datetime import datetime
from dataBase import dbControl
import pandas as pd
import sqlite3

db = dbControl()
db.connect_db()
db.create_vault_table()

#Obtenção do nome do usuário
user = getpass.getuser().upper()

#Controle da tela
class vaultScreen(QMainWindow, Ui_MainWindow):
    
    def __init__(self) -> None:
        super(vaultScreen,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONTROLE DE COFRES")
        self.pushButton_incluir.clicked.connect(lambda:self.new_vault())
        self.pushButton_alterar.clicked.connect(lambda:self.update_vault())
        self.pushButton_excluir.clicked.connect(lambda:self.delete_vault())
        self.pushButton_excel.clicked.connect(lambda:self.excel_generate())
        self.search_vaults()
        
    # PROCURA EMPRESAS E PREENCHE A TABELA
    def search_vaults(self):        
        db = dbControl()
        db.connect_db()
        result = db.select_all_vaults()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate (result):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column,  QTableWidgetItem(str(data)))
                       
        db.connect_close()

        for i in range(1,7):
            self.tableWidget.resizeColumnToContents(i)

    # INCLUI NOVAS EMPRESAS
    def new_vault(self):
        cnpj = self.lnEdit_cnpj.text()
        empresa = self.lnEdit_emp.text()
        rep_legal = self.lnEdit_repLeg.text()
        email = self.lnEdit_email.text()
        venc_mandato = self.calendarWidget.selectedDate().toPython()
        tp_ass = self.cBox_tpAss.currentText()

        if rep_legal == "" or empresa == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ALERTA")
            msg.setText("É necessário preencher o representante legal e a empresa.")
            msg.exec()
            return

        db = dbControl()
        db.connect_db()
        resp = db.insert_vault(cnpj, empresa.upper(), rep_legal.upper(), email, venc_mandato, tp_ass,user.upper())
        self.tableWidget.reset()
        self.search_vaults()
        
        self.lnEdit_cnpj.setText("")
        self.lnEdit_emp.setText("")
        self.lnEdit_repLeg.setText("")
        self.lnEdit_email.setText("")
        self.calendarWidget.selectedDate().toPython()
        self.cBox_tpAss.currentText()

        if resp == "ok":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com Sucesso!")
            
        
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERRO")
            msg.setText("Erro ao cadastrar!")
            

        msg.exec()
        db.connect_close()
    
    # ATUALIZA EMPRESAS
    def update_vault(self):
        data = []
        update_data = []

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                data.append(self.tableWidget.item(row,column).text())
            update_data.append(data)
            data = []
        
        # ATUALIZA DADO NO BANCO

        db = dbControl()
        db.connect_db()

        for vault in update_data:
            db.update_vault(tuple(vault))

        db.connect_close()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("ATUALIZAÇÃO DE DADOS")
        msg.setText("Os dados foram atualizados com sucesso!")
        msg.exec()

    # DELETA EMPRESAS
    def delete_vault(self):
        db = dbControl()
        db.connect_db()

        msg = QMessageBox()
        msg.setWindowTitle("EXCLUIR")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Este registro será excluido!")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_vault(id)
            self.search_vaults()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("SUCESSO!")
            msg.setText(result)
            msg.exec()

    # GERA EXCEL
    def excel_generate():
        db = dbControl()
        db.relat()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = vaultScreen()
    window.showMaximized()
    app.exec()

