from typing import Any, Optional

from ctrl.model import Model


class Guess(Model):
    table_definition: str = """
(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `crsh` TEXT,
    `sinc` INTEGER,
    `till` INTEGER,
    `freq` REAL NOT NULL,
    `type` INTEGER NOT NULL,
    `desc` TEXT,
    `plac` INTEGER NOT NULL,
    `able` INTEGER NOT NULL
)
"""

    # noinspection PyShadowingBuiltins,PyShadowingNames
    def __init__(self,
                 id: int = 0,
                 crsh: Optional[str] = None,
                 sinc: Optional[int] = None,
                 till: Optional[int] = None,
                 freq: float = 0,
                 type: int = 1,
                 desc: Optional[str] = None,
                 plac: Optional[int] = None,
                 able: bool = True):
        self.id: int = id
        self.crsh: Optional[str] = crsh
        self.sinc: Optional[int] = sinc
        self.till: Optional[int] = till
        self.freq: float = freq
        self.type: int = type
        self.desc: Optional[str] = desc
        self.plac: Optional[int] = plac
        self.able: bool = able

    def to_json(self) -> dict:
        ret = dict()
        if self.crsh is not None and len(self.crsh) > 0:
            ret['crsh'] = self.crsh
        if self.sinc is not None:
            ret['sinc'] = self.sinc
        if self.till is not None:
            ret['till'] = self.till
        ret['freq'] = self.freq
        ret['type'] = self.type
        if self.desc is not None and len(self.desc) > 0:
            ret['desc'] = self.desc
        if self.plac is not None:
            ret['plac'] = self.plac
        if not self.able:
            ret['able'] = self.able
        return ret

    @staticmethod
    def from_json(o: dict) -> Any:
        return Guess(
            0,
            o['crsh'] if 'crsh' in o else None,
            o['sinc'] if 'sinc' in o else None,
            o['till'] if 'till' in o else None,
            o['freq'],
            o['type'],
            o['desc'] if 'desc' in o else None,
            o['plac'] if 'plac' in o else None,
            o['able'] if 'able' in o else True,
        )
