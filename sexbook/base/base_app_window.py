import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class BaseAppWindow(Gtk.ApplicationWindow):

    def __init__(self, application: Gtk.Application, title: str):
        super().__init__(application=application, title=title)
        self.c = self.get_application()
        self.set_size_request(800, 600)

    def load_css(self, name: str):
        self.get_style_context() \
            .add_provider(self.c.load_css(name), Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
