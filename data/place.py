from typing import Any, Optional

from sqlalchemy.orm import Mapped, mapped_column

from ctrl.model import Model


class Place(Model):
    __tablename__ = "Place"

    id: Mapped[int] = mapped_column(primary_key=True)
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
    def from_json(o: dict) -> Any:
        return Place(
            id=o['id'],
            name=o['name'] if 'name' in o else None,
            latitude=o['latitude'] if 'latitude' in o else None,
            longitude=o['longitude'] if 'longitude' in o else None,
        )
