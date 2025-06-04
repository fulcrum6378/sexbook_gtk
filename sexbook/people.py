import gi

from sexbook.base import BaseAppWindow, BaseListRow
from sexbook.data import Crush

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class People(BaseAppWindow):

    def __init__(self, application: Gtk.Application):
        super().__init__(application, "people")

        # data
        self.list: list[Crush] = list(self.c.people.values())

        # list_box
        self.list_box = self.ui.get_object("list")
        self.arrangeList()

    def arrangeList(self):
        self.list.sort(key=lambda p: p.vis_name().lower())
        i = 0
        for person in self.list:
            self.list_box.insert(People.Item(self, i, person), -1)  # -1 appends to the end.
            i += 1

    class Item(BaseListRow):
        def __init__(self, c: BaseAppWindow, i: int, person: Crush, **properties):
            super().__init__(c, **properties)
            name = self.ui.get_object("name")
            name.get_buffer().set_text(f"{i + 1}. {person.vis_name()}")
            # FIXME TextViews are not updated after this change!
