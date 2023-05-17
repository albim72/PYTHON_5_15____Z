import mysql.connector

db = mysql.connector.connect(user="root",password="abc123",host='127.0.0.1',port='3306',database="dbtestowa")
cursorObject = db.cursor()
ndata = """
INSERT INTO student(imie,nazwisko,kierunek) VALUES(%s,%s,%s)
"""
jeden = ("Jasio","Kot","Informatyka")
wielu = [
    ("Henryk","Król","Politologia"),
    ("Olga","Nowak","Politologia"),
    ("Maria","Kos","Lekarski"),
    ("Olaf","Krop","Cybernetyka"),
    ("Nadia","Miś","Malarstwo"),
]
cursorObject.execute(ndata,jeden)
cursorObject.executemany(ndata,wielu)
db.commit()
db.close()
