import json

from ctrl.database import Database
from data.crush import Crush
from data.guess import Guess
from data.place import Place
from data.report import Report


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
    def export(db: Database):
        pass

    @staticmethod
    def import_(path: str) -> Exported:
        data: dict = json.load(open(path, 'r', encoding='utf-8'))
        return Exporter.Exported(
            sorted(
                [Report.from_json(i) for i in data['reports']],
                key=lambda i: i.time
            ),
            sorted(
                [Crush.from_json(i) for i in data['crushes']],
                key=lambda i: i.key
            ),
            sorted(
                [Place.from_json(i) for i in data['places']],
                key=lambda i: i.name if i.name is not None else ''
            ),
            sorted(
                sorted(
                    [Guess.from_json(i) for i in data['guesses']],
                    key=lambda i: i.crsh if i.crsh is not None else ''
                ),
                key=lambda i: i.sinc if i.sinc is not None else 0
            ),
            data['settings']
        )

    @staticmethod
    def replace(db: Database, exported: Exported):
        cur = db.con.cursor()
        for report in exported.reports:
            report.insert(cur)
        for crush in exported.crushes:
            crush.insert(cur)
        for place in exported.places:
            place.insert(cur)
        for guess in exported.guesses:
            guess.insert(cur)
        db.con.commit()
