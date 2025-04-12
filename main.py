import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class Main(Gtk.ApplicationWindow):
    """
    :ivar list_box
    """

    def __init__(self, application: Gtk.Application):
        super().__init__(application=application, title="Sexbook")
        self.set_size_request(800, 600)

        # scroller
        scroller: Gtk.ScrolledWindow = Gtk.ScrolledWindow()
        self.set_child(scroller)

        # list_box
        self.list_box: Gtk.ListBox = Gtk.ListBox()
        self.list_box.add_css_class("yellow_box_lister")
        scroller.set_child(self.list_box)
        self.arrangeList()

    def arrangeList(self):
        for i in range(20):
            list_row = Gtk.ListBoxRow()
            self.list_box.insert(list_row, -1)  # -1 appends to the end.

            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            box.set_margin_top(4)
            box.set_margin_bottom(4)
            box.set_margin_start(15)
            box.set_margin_end(15)
            box.add_css_class("yellow_box")
            list_row.set_child(box)

            label = Gtk.Label(label=f"Item {i + 1}")
            box.append(label)
