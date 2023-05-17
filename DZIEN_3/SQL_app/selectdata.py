import mysql.connector

db = mysql.connector.connect(user="root",password="abc123",host='127.0.0.1',port='3306',database="dbtestowa")
cursorObject = db.cursor()
dane = """
SELECT imie,nazwisko,kierunek FROM student
"""

danewhere = """
SELECT imie,nazwisko,kierunek FROM student
WHERE kierunek = 'Politologia'
"""
cursorObject.execute(dane)
mwynik = cursorObject.fetchall()
for x in mwynik:
    print(x)
print("___________________________________")
cursorObject.execute(danewhere)
mwynik = cursorObject.fetchall()
for x in mwynik:
    print(x)

db.close()
