import os

import gi
from sqlalchemy import create_engine, select
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from sexbook.people import People
from sexbook.base import Model
from sexbook.data import *
from sexbook.main import Main

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

    def do_activate(self):
        # load the global CSS
        # noinspection PyArgumentList
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            self.load_css("global"),
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        # launch the main page
        # Main(self).present()
        People(self).present()

    def load_css(self, name: str) -> Gtk.CssProvider:
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(os.path.join(self.resources_dir, "css", f"{name}.css"))
        return css_provider
