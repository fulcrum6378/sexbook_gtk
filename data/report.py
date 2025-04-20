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

    # noinspection PyShadowingBuiltins
    def __init__(self,
                 id: int,
                 time: int,
                 name: Optional[str],
                 type: int,
                 desc: Optional[str],
                 accu: bool,
                 plac: Optional[int],
                 ogsm: bool):
        self.id: int = id
        self.time: int = time
        self.name: Optional[str] = name
        self.type: int = type
        self.desc: Optional[str] = desc
        self.accu: bool = accu
        self.plac: Optional[int] = plac
        self.ogsm: bool = ogsm

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
        if self.plac != -1:
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
            o['desc'] if 'desc' in o else None,
            o['ogsm'] if 'ogsm' in o else True,
        )
