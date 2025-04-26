from typing import Any, Optional

from ctrl.model import Model


class Crush(Model):
    table_definition: str = """
(
    `key` TEXT NOT NULL,
    `first_name` TEXT,
    `middle_name` TEXT,
    `last_name` TEXT,
    `status` INTEGER NOT NULL,
    `birth` TEXT,
    `height` REAL,
    `body` INTEGER NOT NULL,
    `address` TEXT,
    `first_met` TEXT,
    `instagram` TEXT,
    PRIMARY KEY(`key`)
)
"""

    def __init__(self,
                 key: str,
                 first_name: Optional[str] = None,
                 middle_name: Optional[str] = None,
                 last_name: Optional[str] = None,
                 status: int = 0,
                 birth: Optional[str] = None,
                 height: Optional[float] = None,
                 body: int = 0,
                 address: Optional[str] = None,
                 first_met: Optional[str] = None,
                 instagram: Optional[str] = None):
        self.key: str = key
        self.first_name: Optional[str] = first_name
        self.middle_name: Optional[str] = middle_name
        self.last_name: Optional[str] = last_name
        self.status: int = status
        self.birth: Optional[str] = birth
        self.height: Optional[float] = height
        self.body: int = body
        self.address: Optional[str] = address
        self.first_met: Optional[str] = first_met
        self.instagram: Optional[str] = instagram

    def to_json(self) -> dict:
        ret = dict()
        ret['key'] = self.key
        if self.first_name is not None and len(self.first_name) > 0:
            ret['first_name'] = self.first_name
        if self.middle_name is not None and len(self.middle_name) > 0:
            ret['middle_name'] = self.middle_name
        if self.last_name is not None and len(self.last_name) > 0:
            ret['last_name'] = self.last_name
        if self.status != 0:
            ret['status'] = self.status
        if self.birth is not None and len(self.birth) > 0:
            ret['birth'] = self.birth
        if self.height is not None and self.height > 0.0:
            ret['height'] = self.height
        if self.body != 0:
            ret['body'] = self.body
        if self.address is not None and len(self.address) > 0:
            ret['address'] = self.address
        if self.first_met is not None and len(self.first_met) > 0:
            ret['first_met'] = self.first_met
        if self.instagram is not None and len(self.instagram) > 0:
            ret['instagram'] = self.instagram
        return ret

    @staticmethod
    def from_json(o: dict) -> Any:
        return Crush(
            o['key'],
            o['first_name'] if 'first_name' in o else None,
            o['middle_name'] if 'middle_name' in o else None,
            o['last_name'] if 'last_name' in o else None,
            o['status'] if 'status' in o else 0,
            o['birth'] if 'birth' in o else None,
            o['height'] if 'height' in o else None,
            o['body'] if 'body' in o else 0,
            o['address'] if 'address' in o else None,
            o['first_met'] if 'first_met' in o else None,
            o['instagram'] if 'instagram' in o else None,
        )
