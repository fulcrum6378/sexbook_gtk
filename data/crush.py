from ctrl.model import Model


class Crush(Model):
    table_definition: str = """
(
    `key` TEXT NOT NULL,
    `first_name` TEXT,
    `middle_name` TEXT,
    `last_name` TEXT,
    `status` INTEGER NOT NULL,
    `birth` TEXT,
    `height` REAL NOT NULL,
    `body` INTEGER NOT NULL,
    `address` TEXT,
    `first_met` TEXT,
    `instagram` TEXT,
    PRIMARY KEY(`key`)
)
"""
