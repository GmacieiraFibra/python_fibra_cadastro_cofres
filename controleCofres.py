#Bibliotecas necessárioas
from  PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from ui_cofre  import Ui_MainWindow
from ui_novosPoderes import Ui_Form
import sys
import getpass
from datetime import datetime
from dataBase import dbControl

#Obtenção do nome do usuário
user = getpass.getuser().upper()

#Controle da tela
class vaultScreen(QMainWindow, Ui_MainWindow):
    
    def __init__(self) -> None:
        super(vaultScreen,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONTROLE DE COFRES")
        self.pushButton_incluir.clicked.connect(self.callNewPower)

    def callNewPower(self):
        self.w = newPower()
        self.w.showMaximized()
        #self.close()
    
class newPower (QWidget, Ui_Form):
    def __init__(self) -> None:
        super(newPower,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("NOVO PODER")
        self.pButton_salvar.clicked.connect(lambda: self.insertVault())
    
    def insertVault(self):
        cnpj = self.lnEdit_cnpj.text()
        empresa = self.lnEdit_emp.text()
        rep_legal = self.lnEdit_repLeg.text()
        email = self.lnEdit_email.text()
        venc_mandato = self.calendarWidget.selectedDate()
        tp_ass = self.cBox_tpAss.currentText()  

        print(cnpj, empresa, rep_legal, email, venc_mandato, tp_ass)
        db = dbControl()
        db.connect_db()
        db.insert_data(cnpj, empresa, rep_legal, email, venc_mandato, tp_ass)
        db.connect_close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = vaultScreen()
    window.showMaximized()
    app.exec()

