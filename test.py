from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from base import Model
from ctrl import Exporter
from data import Crush

engine: Engine = create_engine("sqlite:///sexbook.db")
Model.metadata.create_all(engine)

with Session(engine) as session:
    Exporter.replace(session, Exporter.import_("sexbook.json"))
    # noinspection PyArgumentList
    print(session.get_one(Crush, "Yuriko").to_json())
