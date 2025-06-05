import json

from sqlalchemy.orm import Session

from sexbook.data import *


class Exporter:
    """
    In charge of exporting and importing data into and out of the Database
    """

    class Exported:
        """
        Represents the structure of an exported JSON file.
        """

        def __init__(self,
                     reports: list[Report],
                     crushes: list[Crush],
                     places: list[Place],
                     guesses: list[Guess],
                     settings: dict):
            self.reports: list[Report] = reports
            self.crushes: list[Crush] = crushes
            self.places: list[Place] = places
            self.guesses: list[Guess] = guesses
            self.settings: dict = settings

    @staticmethod
    def export(session: Session):
        pass  # TODO

    @staticmethod
    def import_(path: str) -> Exported:
        data: dict = json.load(open(path, "r", encoding="utf-8"))
        return Exporter.Exported(
            sorted(
                [Report.from_json(i) for i in data["reports"]],
                key=lambda i: i.time
            ),
            sorted(
                [Crush.from_json(i) for i in data["crushes"]],
                key=lambda i: i.key
            ),
            sorted(
                [Place.from_json(i) for i in data["places"]],
                key=lambda i: i.name if i.name is not None else ""
            ),
            sorted(
                sorted(
                    [Guess.from_json(i) for i in data["guesses"]],
                    key=lambda i: i.crsh if i.crsh is not None else ""
                ),
                key=lambda i: i.sinc if i.sinc is not None else 0
            ),
            data["settings"]
        )

    @staticmethod
    def replace(session: Session, exported: Exported):
        session.add_all(exported.reports)
        session.add_all(exported.crushes)
        session.add_all(exported.places)
        session.add_all(exported.guesses)
        session.commit()
