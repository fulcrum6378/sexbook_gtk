from ctrl.model import Model


class Guess(Model):
    table_definition: str = """
(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `crsh` TEXT,
    `sinc` INTEGER NOT NULL,
    `till` INTEGER NOT NULL,
    `freq` REAL NOT NULL,
    `type` INTEGER NOT NULL,
    `desc` TEXT,
    `plac` INTEGER NOT NULL,
    `able` INTEGER NOT NULL
)
"""
