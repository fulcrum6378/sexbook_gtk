from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from base import Model


class Crush(Model):
    __tablename__ = "Crush"

    key: Mapped[str] = mapped_column(primary_key=True)
    first_name: Mapped[Optional[str]]
    middle_name: Mapped[Optional[str]]
    last_name: Mapped[Optional[str]]
    status: Mapped[int] = mapped_column(default=0)
    birth: Mapped[Optional[str]]
    height: Mapped[Optional[float]]
    body: Mapped[int] = mapped_column(default=0)
    address: Mapped[Optional[str]]
    first_met: Mapped[Optional[str]]
    instagram: Mapped[Optional[str]]

    def vis_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            if self.first_name: return self.first_name
            if self.last_name: return self.last_name
            if self.middle_name: return self.middle_name
            return self.key

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
    def from_json(o: dict):
        return Crush(
            key=o['key'],
            first_name=o['first_name'] if 'first_name' in o else None,
            middle_name=o['middle_name'] if 'middle_name' in o else None,
            last_name=o['last_name'] if 'last_name' in o else None,
            status=o['status'] if 'status' in o else 0,
            birth=o['birth'] if 'birth' in o else None,
            height=o['height'] if 'height' in o else None,
            body=o['body'] if 'body' in o else 0,
            address=o['address'] if 'address' in o else None,
            first_met=o['first_met'] if 'first_met' in o else None,
            instagram=o['instagram'] if 'instagram' in o else None,
        )
