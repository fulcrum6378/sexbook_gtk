from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from base import Model


class Report(Model):
    __tablename__ = "Report"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    time: Mapped[int]
    name: Mapped[Optional[str]]
    type: Mapped[int] = mapped_column(default=1)
    desc: Mapped[Optional[str]]
    accu: Mapped[bool] = mapped_column(default=True)
    plac: Mapped[Optional[int]]
    ogsm: Mapped[bool] = mapped_column(default=True)

    # noinspection PyAttributeOutsideInit
    def analyse(self):
        self.analysis = map(
            lambda s: s.strip(),
            (self.name.replace(" and ", " + ")
             .replace(" & ", " + ")
             .replace(", ", " + ")
             .split(" + "))
        ) if self.name else list()

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
    def from_json(o: dict):
        return Report(
            time=o['time'],
            name=o['name'] if 'name' in o else None,
            type=o['type'],
            desc=o['desc'] if 'desc' in o else None,
            accu=o['accu'] if 'accu' in o else True,
            plac=o['plac'] if 'plac' in o else None,
            ogsm=o['ogsm'] if 'ogsm' in o else True,
        )
