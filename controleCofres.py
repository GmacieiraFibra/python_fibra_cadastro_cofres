#Bibliotecas necessárioas
from  PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_cofre  import Ui_MainWindow
import sys
import getpass
#import db_control
from datetime import datetime

#Obtenção do nome do usuário
user = getpass.getuser().upper()

#Controle da tela
class regScreen(QMainWindow, Ui_MainWindow):
    
    def __init__(self) -> None:
        super(regScreen,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ATIVIDADES HABILITAÇÃO")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = regScreen()
    window.show()
    app.exec()

