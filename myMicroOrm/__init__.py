import sqlite3


class MyMicroORM(sqlite3):
    def __init__(self, database, table):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect.cursor()
        self.table = table

    def MainQuery(self, query, tuple):
        self.cursor.execute(query, tuple)
        response_list = self.cursor.fetchall()
        self.connect.commit()
        return response_list
