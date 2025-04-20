from abc import ABC, abstractmethod
from io import UnsupportedOperation
from json import JSONEncoder
from typing import Any


class Model(ABC):
    table_definition: str

    @abstractmethod
    def to_json(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_json(obj: dict) -> Any:
        pass

    class Encoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, Model):
                return o.to_json()
            raise UnsupportedOperation("Encoding " + o.__name__ + " is not supported.")
