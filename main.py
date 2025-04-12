import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class Main(Gtk.ApplicationWindow):
    def __init__(self, application: Gtk.Application):
        super().__init__(application=application, title="Sexbook")
        self.set_size_request(800, 600)
