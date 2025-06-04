import gi

from .base_app_window import BaseAppWindow

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class BaseListRow(Gtk.ListBoxRow):
    """
    :ivar c any `BaseAppWindow` application window context
    """

    def __init__(self, c: BaseAppWindow, **properties):
        super().__init__(**properties)
        self.c = c

        self.ui = self.c.c.load_ui(f"{self.c.id}_item")
        self.set_child(self.ui.get_objects()[0])
