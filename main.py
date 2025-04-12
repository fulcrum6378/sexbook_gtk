import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class Main(Gtk.ApplicationWindow):
    """
    :ivar scroller
    :ivar list_box
    """

    def __init__(self, application: Gtk.Application):
        super().__init__(application=application, title="Sexbook")
        self.set_size_request(800, 600)

        # scroller
        self.scroller: Gtk.ScrolledWindow = Gtk.ScrolledWindow()
        self.set_child(self.scroller)

        # list_box
        self.list_box: Gtk.ListBox = Gtk.ListBox()
        self.scroller.set_child(self.list_box)
        self.arrangeList()

    def arrangeList(self):
        for i in range(20):
            list_row = Gtk.ListBoxRow()
            self.list_box.insert(list_row, -1)  # -1 appends to the end.

            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            box.add_css_class("yellow_box")
            list_row.set_child(box)

            label = Gtk.Label(label=f"Item {i + 1}")
            label.set_hexpand(True)  # expand horizontally
            label.set_vexpand(True)  # expand vertically
            label.set_margin_start(0)
            label.set_margin_end(0)
            box.append(label)
