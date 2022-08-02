import os
import sqlite3


class MyMicroORM(sqlite3.Connection):
    def __init__(self, db_path):
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()
        if self.db_not_exists():
            self.init_db()

    def MainQuery(self, query, data, many=False):
        if many:
            self.cursor.executemany(query, data)
        else:
            self.cursor.execute(query, data)
        response_list = self.cursor.fetchall()
        self.connect.commit()
        return response_list

    def init_db(self):
        with open(os.path.join("install", "createdb.sql"), "r") as f:
            sql = f.read()
        self.cursor.executescript(sql)
        self.connect.commit()

    def db_not_exists(self):
        """Проверяет, инициализирована ли БД, если нет — инициализирует"""
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='farms_id'"
        )
        if self.cursor.fetchall():
            return False
        return True

    def add(self, table, values, many=False):
        if many:
            qmarks = self.get_question_marks(values[0])
        else:
            qmarks = self.get_question_marks(values)
        query = f"INSERT OR IGNORE INTO {table} VALUES ({qmarks})"
        self.MainQuery(query, values, many)

    def upd(self, table, values, filters=None):
        pass

    def get(self, table, values, filters=None):
        pass

    def get_question_marks(self, values):
        return ("".join(["?," for _ in range(len(values))]))[:-1]
