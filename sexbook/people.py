import gi

from sexbook.base import BaseAppWindow
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
            list_row = Gtk.ListBoxRow()
            self.list_box.insert(list_row, -1)  # -1 appends to the end.

            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            box.set_margin_top(4)
            box.set_margin_bottom(4)
            box.set_margin_start(15)
            box.set_margin_end(15)
            box.add_css_class("yellow_box")
            list_row.set_child(box)

            label = Gtk.Label(label=f"{i + 1}. {person.vis_name()}")
            box.append(label)

            i += 1
