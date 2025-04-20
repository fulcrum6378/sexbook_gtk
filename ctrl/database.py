import sqlite3
from sqlite3.dbapi2 import Connection
from typing import Type

from ctrl.model import Model
from data.report import Report
from data.crush import Crush
from data.place import Place
from data.guess import Guess


# noinspection SqlNoDataSourceInspection,SqlResolve
class Database:
    """
    :ivar con: the main connection to our one and only SQLite database
    """

    def __init__(self):
        self.con: Connection = sqlite3.connect("sexbook.db")

        for model in [Report, Crush, Place, Guess]:
            self.__ensure_table_exists(model)

    def __ensure_table_exists(self, model: Type[Model]):
        if self.__check_if_table_exists(model.__name__): return
        print("Creating table " + model.__name__ + "...")
        cur = self.con.cursor()
        cur.execute("CREATE TABLE " + model.__name__ + model.table_definition)
        self.con.commit()
        cur.close()

    def __check_if_table_exists(self, table_name: str):
        cur = self.con.cursor()
        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)
        )
        ret = not not cur.fetchone()
        cur.close()
        return ret

    def close(self):
        self.con.close()
