import time
from sqlite3 import Cursor
from typing import Any, Optional

from ctrl.model import Model


class Report(Model):
    table_definition: str = """
(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `time` INTEGER NOT NULL,
    `name` TEXT,
    `type` INTEGER NOT NULL,
    `desc` TEXT,
    `accu` INTEGER NOT NULL,
    `plac` INTEGER,
    `ogsm` INTEGER NOT NULL
)
"""

    # noinspection PyShadowingBuiltins,PyShadowingNames
    def __init__(self,
                 id: int = 0,
                 time: int = time.time() * 1000,
                 name: Optional[str] = None,
                 type: int = 1,
                 desc: Optional[str] = None,
                 accu: bool = True,
                 plac: Optional[int] = None,
                 ogsm: bool = True):
        self.id: int = id
        self.time: int = time
        self.name: Optional[str] = name
        self.type: int = type
        self.desc: Optional[str] = desc
        self.accu: bool = accu
        self.plac: Optional[int] = plac
        self.ogsm: bool = ogsm

    @staticmethod
    def query(id: Any, cursor: Cursor) -> Any:
        cursor.execute("SELECT * FROM Report WHERE id = " + id + " LIMIT 1")
        cursor.fetchone()

    def insert(self, cursor: Cursor):
        cursor.execute("INSERT INTO Report")

    def update(self, cursor: Cursor):
        cursor.execute("")

    def delete(self, cursor: Cursor):
        cursor.execute("")

    def to_json(self) -> dict:
        ret = dict()
        ret['time'] = self.time
        if self.name is not None and len(self.name) > 0:
            ret['name'] = self.name
        ret['type'] = self.type
        if self.desc is not None and len(self.desc) > 0:
            ret['desc'] = self.desc
        if not self.accu:
            ret['accu'] = self.accu
        if self.plac is not None:
            ret['plac'] = self.plac
        if not self.ogsm:
            ret['ogsm'] = self.ogsm
        return ret

    @staticmethod
    def from_json(o: dict) -> Any:
        return Report(
            0,
            o['time'],
            o['name'] if 'name' in o else None,
            o['type'],
            o['desc'] if 'desc' in o else None,
            o['accu'] if 'accu' in o else True,
            o['plac'] if 'plac' in o else None,
            o['ogsm'] if 'ogsm' in o else True,
        )
