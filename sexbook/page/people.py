import gi

from sexbook.base import BaseListItem, BasePage
from sexbook.data import Crush

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class People(BasePage):
    """
    :ivar ui_list
    """

    def __init__(self, application: Gtk.Application):
        super().__init__(application, "people")

        # data
        self.list: list[Crush] = list(self.c.people.values())

        # listing
        self.ui_list = self.ui.get_object("list")
        self.arrangeList()

    def arrangeList(self):
        self.list.sort(key=lambda p: p.vis_name().lower())
        i = 0
        for person in self.list:
            self.ui_list.insert(People.Item(self, i, person), -1)  # -1 appends to the end.
            i += 1

    class Item(BaseListItem):
        def on_create_item(self, i: int, data: Crush):
            self.ui.get_object("name").set_text(f"{i + 1}. {data.vis_name()}")
