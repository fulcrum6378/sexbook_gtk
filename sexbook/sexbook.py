import os

import gi
import yaml
from sqlalchemy import create_engine, select
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from sexbook.base import Model
from sexbook.data import *
from sexbook.page import Main

gi.require_version("Gtk", "4.0")
from gi.repository import Gdk, GLib, Gtk


class Sexbook(Gtk.Application):
    """
    :ivar resources_dir
    :ivar data_dir

    :ivar db: SQLAlchemy database engine
    :ivar reports: all [Report] instances in the database
    :ivar people: all [Crush] instances in the database
    :ivar places: all [Place] instances in the database
    :ivar guesses: all [Guess] instances in the database

    :ivar lang ISO code of the current language
    :ivar dictionary containing all translations
    """

    # noinspection PyTypeChecker
    def __init__(self):
        super().__init__(application_id="ir.mahdiparastesh.Sexbook")
        GLib.set_application_name("Sexbook")

        # necessary fields
        self.resources_dir: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources")
        self.data_dir: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

        # initialise the database
        self.db: Engine = create_engine("sqlite:///data/sexbook.db")
        Model.metadata.create_all(self.db)

        # load the entire database (all necessary!)
        with Session(self.db) as session:
            self.reports: dict[Report] = \
                dict(map(lambda r: (r.id, r), session.scalars(select(Report)).all()))
            self.people: dict[Crush] = \
                dict(map(lambda p: (p.key, p), session.scalars(select(Crush)).all()))
            self.places: list[Place] = session.scalars(select(Place)).all()
            self.guesses: list[Guess] = session.scalars(select(Guess)).all()

        # load translations
        self.lang = "en"
        self.dictionary = yaml.safe_load(open(os.path.join("resources", "lang", self.lang + ".yaml"), "r").read())

    def do_activate(self):
        # load the global CSS
        self.load_css("global")

        # launch the `Main` page
        Main(self).present()

    def load_ui(self, name: str) -> Gtk.Builder:
        builder = Gtk.Builder()
        builder.add_from_file(os.path.join(self.resources_dir, "ui", f"{name}.ui"))
        return builder

    def load_css(self, name: str) -> None:
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(os.path.join(self.resources_dir, "css", f"{name}.css"))
        # noinspection PyArgumentList
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def text(self, text_id: str) -> str | list[str]:
        return self.dictionary[text_id]
