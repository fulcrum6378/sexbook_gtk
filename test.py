from ctrl.database import Database
from ctrl.exporter import Exporter

Database().close()
Exporter.import_("sexbook.json")
