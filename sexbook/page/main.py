from typing import Optional

import gi

from sexbook.base import BasePage, BaseListItem
from sexbook.data import Report

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class Main(BasePage):
    """
    :ivar filters a list of all `Report.Filter`s
    :ivar filter index of the chosen `Report.Filter` out of `filters`

    :ivar ui_list displays `Report.Filter.reports`
    :ivar ui_filter displays `filters`
    """

    def on_create(self):
        self.filters: list[Report.Filter] = []
        self.filter: Optional[int] = None

        self.ui_list: Gtk.ListBox = self.ui.get_object("list")
        self.ui_filter: Gtk.DropDown = self.ui.get_object("filter")

        # do the filtering and listing
        self.reset()

    def reset(self):

        # create filters and pick one
        self.create_filters()
        self.filter = -1 if self.filter is None else self.filter

        # display filters in the UI
        filter_names = list()
        i = 1
        months = self.c.text("gregorianMonths")
        for f in self.filters:
            filter_names.append(f"{i}. {months[f.month - 1]} {f.year} : {{{len(f.reports)}}}")
            i += 1
        # noinspection PyTypeChecker
        self.ui_filter.set_model(Gtk.StringList.new(filter_names))
        self.ui_filter.set_selected(self.filter if self.filter >= 0 else len(self.filters) + self.filter)

        # arrange a list
        self.arrangeList()

    def create_filters(self):
        self.filters = []
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
            self.ui_list.insert(Main.Item(self, 0, self.c.reports[r_id]), -1)  # -1 appends to the end.

    class Item(BaseListItem):
        def on_create_item(self, i: int, report: Report):
            self.ui.get_object("name").set_text(report.name)
