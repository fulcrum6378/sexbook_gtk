import gi

from sexbook.base import BaseListItem, BasePage
from sexbook.data import Crush

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class People(BasePage):
    """
    :ivar list a changeable list of all `Crush`es being shown in `ui_list`

    :ivar ui_list displays `list`
    """

    def on_create(self):
        self.list: list[Crush] = list(self.c.people.values())

        self.ui_list: Gtk.ListBox = self.ui.get_object("list")

        # do the listing
        self.arrangeList()

    def arrangeList(self):
        self.list.sort(key=lambda p: p.vis_name().lower())
        i = 0
        for person in self.list:
            self.ui_list.insert(People.Item(self, i, person), -1)  # -1 appends to the end.
            i += 1

    class Item(BaseListItem):
        def on_create_item(self, i: int, person: Crush):
            self.ui.get_object("name").set_text(f"{i + 1}. {person.vis_name()}")
