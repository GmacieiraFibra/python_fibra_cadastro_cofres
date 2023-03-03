import sqlite3
from sqlite3 import Error as err
import pandas as pd
import tkinter
from tkinter import filedialog


class dbControl():
    def __init__(self, name = "vault.db") -> None:
        self.name = name
    
    def connect_db(self):
        self.connection = sqlite3.connect(self.name)

    def connect_close(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_vault_table(self):
        try:    
            cur = self.connection.cursor ()
            cur.execute("""

                CREATE TABLE IF NOT EXISTS vaults(                
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    cnpj TEXT NOT NULL,
                    empresa TEXT NOT NULL,
                    rep_legal TEXT NOT NULL,
                    email TEXT NOT NULL,
                    venc_mandato DATE NOT NULL,
                    tp_ass TEXT NOT NULL,
                    user TEXT NOT NULL
                )                
            """)
            cur.close()
        except:
            print(err)
        
    def insert_vault(self, cnpj, empresa, rep_legal, email, venc_mandato, tp_ass, user):
        try:
            cur = self.connection.cursor()
            cur.execute("""
            INSERT INTO vaults(cnpj, empresa, rep_legal, email, venc_mandato, tp_ass,user) VALUES (?,?,?,?,?,?,?)
            """, (cnpj, empresa, rep_legal, email, venc_mandato, tp_ass, user))

            self.connection.commit()
            return ("ok")
        except:
             print(err)

    def select_all_vaults(self):
        try:
            cur=self.connection.cursor()
            cur.execute("""SELECT * FROM vaults""")
            vaults = cur.fetchall()
            return vaults
        except:
            pass

    def vanquished(self, today):
        try:
            cur=self.connection.cursor()
            cur.execute(f"""SELECT * FROM vaults where venc_mandato < '{today}' """)
            vaults = cur.fetchall()
            return vaults
        except:
            pass

    def future_maturities(self, today, qt_days):
        try:
            cur=self.connection.cursor()
            cur.execute(f"""SELECT * FROM vaults where venc_mandato BETWEEN '{today}' AND '{qt_days}' """)
            vaults = cur.fetchall()
            return vaults
        except:
            pass

    def delete_vault(self,id):
        try:
            cur=self.connection.cursor()
            cur.execute(f"""DELETE FROM vaults WHERE id = {id}""")

            self.connection.commit()
            
            return "O registro foi excluído com sucesso!"
        
        except:
            return("Erro ao excluir")
    
    def update_vault(self, fullDataSet):
            
        cur=self.connection.cursor()
        cur.execute(f"""UPDATE vaults set
            id = {fullDataSet[0]}, 
            cnpj = '{fullDataSet[1]}', 
            empresa = '{fullDataSet[2]}', 
            rep_legal = '{fullDataSet[3]}', 
            email = '{fullDataSet[4]}', 
            venc_mandato = '{fullDataSet[5]}', 
            tp_ass = '{fullDataSet[6]}'

            WHERE id = {fullDataSet[0]}              
            """)
        self.connection.commit()

if __name__ == "__main__":
    db = dbControl()
    db.connect_db()
    db.create_vault_table()
    db.connect_close()