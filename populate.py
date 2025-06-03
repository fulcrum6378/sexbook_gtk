import os

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from sexbook.base import Model
from sexbook.ctrl import Exporter
from sexbook.data import Crush

engine: Engine = create_engine(f"sqlite:///data/sexbook.db")
Model.metadata.create_all(engine)

with Session(engine) as session:
    Exporter.replace(session, Exporter.import_("data/sexbook.json"))
    # noinspection PyArgumentList
    print(session.get_one(Crush, "Yuriko").to_json())
