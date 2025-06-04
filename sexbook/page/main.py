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

    :ivar list_box
    """

    def __init__(self, application: Gtk.Application):
        super().__init__(application, "main")

        # default fields
        self.filters: set[Report.Filter] = set()
        self.filter: Optional[Report.Filter] = None

        # root layout
        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(root)
        cl = Gtk.ConstraintLayout()
        self.set_layout_manager(cl)

        # list layout
        scroller = Gtk.ScrolledWindow()
        root.append(scroller)
        self.list_box: Gtk.ListBox = Gtk.ListBox()
        self.list_box.add_css_class("yellow_box_lister")
        scroller.set_child(self.list_box)

        # dropdown
        dropdown = Gtk.DropDown()
        dropdown.set_model(Gtk.StringList.new(["Option A", "Option B", "Option C"]))
        root.append(dropdown)

        # layout constraints
        cl.add_constraint(
            Gtk.Constraint.new(
                dropdown, Gtk.ConstraintAttribute.BOTTOM,
                Gtk.ConstraintRelation.EQ,
                root, Gtk.ConstraintAttribute.BOTTOM,
                12, 12, Gtk.ConstraintStrength.REQUIRED)
        )

        # begin filtering and arranging
        self.reset()

    def reset(self):
        self.create_filters()
        self.filter = list(self.filters)[-1 if self.filter is None else self.filter]
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
        self.filter.reports.sort(key=lambda r_id: self.c.reports[r_id].time)
        for r_id in self.filter.reports:
            report = self.c.reports[r_id]

            list_row = Gtk.ListBoxRow()
            self.list_box.insert(list_row, -1)  # -1 appends to the end.

            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            box.set_margin_top(4)
            box.set_margin_bottom(4)
            box.set_margin_start(15)
            box.set_margin_end(15)
            box.add_css_class("yellow_box")
            list_row.set_child(box)

            label = Gtk.Label(label=report.name)
            box.append(label)
