from abc import ABC, abstractmethod
from io import UnsupportedOperation
from json import JSONEncoder
from sqlite3.dbapi2 import Cursor
from typing import Any


class Model(ABC):
    table_definition: str

    @staticmethod
    @abstractmethod
    def query(id: Any, cursor: Cursor) -> Any:
        pass

    @abstractmethod
    def insert(self, cursor: Cursor):
        pass

    @abstractmethod
    def update(self, cursor: Cursor):
        pass

    @abstractmethod
    def delete(self, cursor: Cursor):
        pass

    @abstractmethod
    def to_json(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_json(o: dict) -> Any:
        pass

    class Encoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, Model):
                return o.to_json()
            raise UnsupportedOperation("Encoding " + o.__name__ + " is not supported.")
