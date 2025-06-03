from abc import abstractmethod
from io import UnsupportedOperation
from json import JSONEncoder

from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):

    @abstractmethod
    def to_json(self) -> dict:
        """
        Don't call this method before SQLAlchemy processes an instance of this class.
        """
        pass

    @staticmethod
    @abstractmethod
    def from_json(o: dict):
        pass

    class Encoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, Model):
                return o.to_json()
            raise UnsupportedOperation("Encoding " + o.__name__ + " is not supported.")
