import mysql.connector

db = mysql.connector.connect(user="root",password="abc123",host='127.0.0.1',port='3306',database="dbtestowa")
cursorObject = db.cursor()
ntab = """
CREATE TABLE IF NOT EXISTS student(
idstudenta int auto_increment primary key,
imie varchar(40),
nazwisko varchar(40),
kierunek varchar(100)
);
"""
cursorObject.execute(ntab)
db.close()
