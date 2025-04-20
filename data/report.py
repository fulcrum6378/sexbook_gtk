from ctrl.model import Model


class Report(Model):
    table_definition: str = """
(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `time` INTEGER NOT NULL,
    `name` TEXT,
    `type` INTEGER NOT NULL,
    `desc` TEXT,
    `accu` INTEGER NOT NULL,
    `plac` INTEGER NOT NULL,
    `ogsm` INTEGER NOT NULL
)
"""
