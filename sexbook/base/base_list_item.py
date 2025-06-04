from abc import abstractmethod
from typing import Any

import gi

from .base_page import BasePage

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class BaseListItem(Gtk.ListBoxRow):
    """
    :ivar c `BasePage` context
    """

    def __init__(self, c: BasePage, i: int, data: Any, **properties):
        super().__init__(**properties)
        self.c = c

        self.ui = self.c.c.load_ui(f"{self.c.id}_item")
        self.on_create_item(i, data)
        self.set_child(self.ui.get_objects()[0])

    @abstractmethod
    def on_create_item(self, i: int, data: Any):
        pass
