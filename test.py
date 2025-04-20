from ctrl.database import Database
from ctrl.exporter import Exporter

db = Database()
Exporter.replace(db, Exporter.import_("sexbook.json"))
db.close()
