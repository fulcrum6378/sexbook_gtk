from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from base import Model


class Place(Model):
    __tablename__ = "Place"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)  # must never be altered
    name: Mapped[Optional[str]]
    latitude: Mapped[Optional[float]]
    longitude: Mapped[Optional[float]]

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
    def from_json(o: dict):
        return Place(
            id=o['id'],  # must never be altered
            name=o['name'] if 'name' in o else None,
            latitude=o['latitude'] if 'latitude' in o else None,
            longitude=o['longitude'] if 'longitude' in o else None,
        )
