from typing import Optional

import gi

from sexbook.base import BasePage
from sexbook.data import Report

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class Main(BasePage):
    """
    :ivar filters a list of all `Report.Filter`s
    :ivar filter a `Report.Filter` chosen out of the list of `filters`

    :ivar ui_list
    :ivar ui_filter
    """

    def __init__(self, application: Gtk.Application):
        super().__init__(application, "main")

        # default fields
        self.filters: list[Report.Filter] = []
        self.filter: Optional[int] = None

        # root layout
        # root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # self.set_child(root)
        # cl = Gtk.ConstraintLayout()
        # self.set_layout_manager(cl)

        # list layout
        # scroller = Gtk.ScrolledWindow()
        # root.append(scroller)
        # self.list_box: Gtk.ListBox = Gtk.ListBox()
        # self.list_box.add_css_class("yellow_box_lister")
        # scroller.set_child(self.list_box)

        # dropdown
        # dropdown = Gtk.DropDown()
        # dropdown.set_model(Gtk.StringList.new(["Option A", "Option B", "Option C"]))
        # root.append(dropdown)

        # listing
        self.ui_list = self.ui.get_object("list")
        self.ui_filter = self.ui.get_object("filter")
        self.reset()

    def reset(self):

        # create filters and pick one
        self.create_filters()
        self.filter = -1 if self.filter is None else self.filter

        # display filters in the UI
        filter_names = list()
        i = 1
        for f in self.filters:
            filter_names.append(f"{i}. {f.month} . {f.year}")
            i += 1
        # noinspection PyTypeChecker
        self.ui_filter.set_model(Gtk.StringList.new(filter_names))

        # arrange a list
        self.arrangeList()

    def create_filters(self):
        self.filters = list()
        for id, r in self.c.reports.items():
            f = Report.Filter.from_timestamp(r.time)
            try:
                index = self.filters.index(f)
                f = self.filters[index]
            except ValueError:
                self.filters.append(f)
            f.reports.append(id)
        self.filters.sort()

    # noinspection PyShadowingNames
    def arrangeList(self):
        current_filter = self.filters[self.filter]
        current_filter.reports.sort(key=lambda r_id: self.c.reports[r_id].time)

        for r_id in current_filter.reports:
            report = self.c.reports[r_id]

            list_row = Gtk.ListBoxRow()
            self.ui_list.insert(list_row, -1)  # -1 appends to the end.

            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            box.set_margin_top(4)
            box.set_margin_bottom(4)
            box.set_margin_start(15)
            box.set_margin_end(15)
            box.add_css_class("yellow_box")
            list_row.set_child(box)

            label = Gtk.Label(label=report.name)
            box.append(label)
