from abc import abstractmethod

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class BasePage(Gtk.ApplicationWindow):
    """
    :ivar c `Sexbook` application context
    :ivar id a unique short string identifier for this page
    :ivar ui `Gtk.Builder` having loaded the default UI of this page
    """

    def __init__(self, application: Gtk.Application):
        self.id = self.__class__.__name__.lower()
        super().__init__(application=application,
                         title=(application.text("app_name") +
                                (f" - {application.text(self.id)}" if self.id != "main" else "")))
        self.c = self.get_application()
        self.set_size_request(800, 600)

        # load UI
        self.ui = self.c.load_ui(self.id)
        self.set_child(self.ui.get_objects()[0])

        # inheritor customisations
        self.on_create()

    @abstractmethod
    def on_create(self):
        pass

    def load_css(self, name: str):
        self.get_style_context() \
            .add_provider(self.c.load_css(name), Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
