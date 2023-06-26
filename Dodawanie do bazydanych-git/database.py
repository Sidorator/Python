import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS uczen (ulica varchar(20) primary key, dom varchar(20), kod varchar(2))")
        self.conn.commit()

    def fetch_all(self):
        self.c.execute("SELECT * FROM uczen")
        rows = self.c.fetchall()
        return rows

    def get_record_by_id(self, id):
        self.c.execute("SELECT * FROM uczen WHERE id=?", (id,))
        row = self.c.fetchone()
        return row

    def insert(self, ulica, dom, kod):
        self.c.execute("INSERT INTO uczen VALUES (?,?,?, ?);", (ulica, dom, kod))
        self.conn.commit()


    def delete(self):
        self.c.execute("DELETE FROM uczen")
        self.conn.commit()


    def update(self, imie, nazwisko, klasa):
        self.c.execute("UPDATE uczen SET imie=?, nazwisko=?, klasa = ? WHERE id=?", (imie, nazwisko, klasa))
        self.conn.commit()

    def get_record_by_id(self):
        self.c.execute("SELECT")


def __del__(self):
    self.conn.close()