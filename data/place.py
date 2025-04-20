from ctrl.model import Model


class Place(Model):
    table_definition: str = """
(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `name` TEXT,
    `latitude` REAL NOT NULL,
    `longitude` REAL NOT NULL
)
"""
