import sqlite3
from sqlite3 import Error as err

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
        
    def insert_data(self, cnpj, empresa, rep_legal, email, venc_mandato, tp_ass):
        try:
            cur = self.connection.cursor()
            cur.execute("""
            INSERT INTO vaults(cnpj, empresa, rep_legal, email, venc_mandato, tp_ass) VALUES (?,?,?,?,?,?)
            """, (cnpj, empresa, rep_legal, email, venc_mandato, tp_ass))

            self.connection.commit()
        except:
            print("deu ruim")

if __name__ == "__main__":
    db = dbControl()
    db.connect_db()
    db.create_vault_table()
    db.connect_close()