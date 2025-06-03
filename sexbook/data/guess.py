from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from sexbook.base import Model


class Guess(Model):
    __tablename__ = "Guess"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    crsh: Mapped[Optional[str]]
    sinc: Mapped[Optional[int]]
    till: Mapped[Optional[int]]
    freq: Mapped[float] = mapped_column(default=0)
    type: Mapped[int] = mapped_column(default=1)
    desc: Mapped[Optional[str]]
    plac: Mapped[Optional[int]]
    able: Mapped[bool]

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
    def from_json(o: dict):
        return Guess(
            crsh=o['crsh'] if 'crsh' in o else None,
            sinc=o['sinc'] if 'sinc' in o else None,
            till=o['till'] if 'till' in o else None,
            freq=o['freq'],
            type=o['type'],
            desc=o['desc'] if 'desc' in o else None,
            plac=o['plac'] if 'plac' in o else None,
            able=o['able'] if 'able' in o else True,
        )
