from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from data.crush import Crush
from data.guess import Guess
from data.place import Place
from data.report import Report

engine: Engine = create_engine("sqlite:///sexbook.db")

with Session(engine) as session:
    # session.add(Crush(key="YURIKO"))
    # session.commit()
    print(session.get_one(Crush, "YURIKO").to_json())

# from ctrl.database import Database
# from ctrl.exporter import Exporter

# db = Database()
# Exporter.replace(db, Exporter.import_("sexbook.json"))
# db.close()
