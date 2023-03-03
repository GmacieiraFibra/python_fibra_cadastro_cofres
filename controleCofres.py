#Bibliotecas necessárioas
from  PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QMessageBox)
import PySide6.QtCore
from ui_cofre  import Ui_MainWindow
import openpyxl
import sys
import getpass
import datetime
from dataBase import dbControl
import pandas as pd
import sqlite3
import tkinter 
from tkinter import filedialog


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
        self.actionFechar.triggered.connect(lambda:self.screen_close())
        self.actionRelat_rio_Excel.triggered.connect(lambda:self.excel_generate_full())
        self.pushButton_incluir.clicked.connect(lambda:self.new_vault())
        self.pushButton_alterar.clicked.connect(lambda:self.update_vault())
        self.pushButton_excluir.clicked.connect(lambda:self.delete_vault())
        self.pushButton_excel.clicked.connect(lambda:self.excel_generate()) 
        self.pushButton_30.clicked.connect(lambda:self.future_maturities(30))
        self.pushButton_15.clicked.connect(lambda:self.future_maturities(15))
        self.pushButton_vencidos.clicked.connect(lambda:self.vanquishe())       
        self.pushButton_LimpaFiltro.clicked.connect(lambda:self.filter_clear())
        self.search_vaults()
        
    # PROCURAR EMPRESAS E PREENCHE A TABELA
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

    # INCLUIR NOVAS EMPRESAS
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
    
    # ATUALIZAR EMPRESAS
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

    # GERAR EXCEL
    def excel_generate(self):
    
        data =[]
        all_data = []

        for row in range (self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                data.append(self.tableWidget.item(row, column).text())
            all_data.append(data)
            data=[]
        
        columns=  ['id','cnpj', 'empresa', 'rep_legal', 'email', 'venc_mandato', 'tp_ass']

        vaults = pd.DataFrame(all_data, columns=columns)
        root = tkinter.Tk()
        dirNome = filedialog.askdirectory(parent=root, initialdir="/",title ='Selecione a pasta')
        vaults.to_excel(dirNome +"\\Cofres.xlsx", sheet_name="Cofres", index= False)
        root.withdraw()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("SUCESSO!")
        msg.setText(f"Relatório gerado com sucesso em {dirNome}!")
        msg.exec()

    # FECHAR PROGRAMA
    def screen_close (self):
            self.close()

    # GERAR EXCEL FULL
    def excel_generate_full(self):
        conn = sqlite3.connect('vault.db')
        result= pd.read_sql_query("SELECT * FROM vaults", conn)

        root = tkinter.Tk()
        dirNome = filedialog.askdirectory(parent=root, initialdir="/",title ='Selecione a pasta')
        result.to_excel(dirNome +"\\Cofres completo.xlsx",sheet_name="Rel_Cofres", index=False)
        root.withdraw()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("SUCESSO!")
        msg.setText(f"Relatório gerado com sucesso em {dirNome}!")
        msg.exec()

    # LIMPA FILTROS
    def filter_clear(self):
        self.tableWidget.reset()
        self.search_vaults()

    # FILTRAR VENCIDAS
    def vanquishe(self):
        db = dbControl()
        db.connect_db()
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        result = db.vanquished(today)
        db.connect_close()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate (result):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column,  QTableWidgetItem(str(data)))
                       
        db.connect_close()

        for i in range(1,7):
            self.tableWidget.resizeColumnToContents(i)
        
        msg = QMessageBox()
        msg.setWindowTitle("RESULTADO")
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText(f"Foram encontrados {len(result)} registros com poderes vecidos")
        msg.exec()

    # FILTRAR VENCIMENTOS FUTUROS
    def future_maturities(self, qt_d):
        db = dbControl()
        db.connect_db()
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        qt_days = datetime.datetime.today() + datetime.timedelta(qt_d)
        qt_days = qt_days.strftime('%Y-%m-%d')
        result = db.future_maturities(today, qt_days)
        db.connect_close()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate (result):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column,  QTableWidgetItem(str(data)))
                       
        db.connect_close()

        for i in range(1,7):
            self.tableWidget.resizeColumnToContents(i)

        msg = QMessageBox()
        msg.setWindowTitle("RESULTADO")
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText(f"Foram encontrados {len(result)} registros com vencimento para {qt_d} dias")
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = vaultScreen()
    window.showMaximized()
    app.exec()

