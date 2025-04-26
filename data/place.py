from typing import Any, Optional

from ctrl.model import Model


class Place(Model):
    table_definition: str = """
(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `name` TEXT,
    `latitude` REAL,
    `longitude` REAL
)
"""

    # noinspection PyShadowingBuiltins
    def __init__(self,
                 id: int = 0,
                 name: Optional[str] = None,
                 latitude: Optional[float] = None,
                 longitude: Optional[float] = None):
        self.id: int = id
        self.name: Optional[str] = name
        self.latitude: Optional[float] = latitude
        self.longitude: Optional[float] = longitude

    def to_json(self) -> dict:
        ret = dict()
        ret['id'] = self.id
        if self.name is not None and len(self.name) > 0:
            ret['name'] = self.name
        if self.latitude is not None:
            ret['latitude'] = self.latitude
        if self.longitude is not None:
            ret['longitude'] = self.longitude
        return ret

    @staticmethod
    def from_json(o: dict) -> Any:
        return Place(
            o['id'],
            o['name'] if 'name' in o else None,
            o['latitude'] if 'latitude' in o else None,
            o['longitude'] if 'longitude' in o else None,
        )
