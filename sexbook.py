import sys
from typing import Optional

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

from main import Main


class Sexbook(Gtk.Application):
    """
    :ivar main: the `Main` window
    """

    def __init__(self):
        super().__init__(application_id="ir.mahdiparastesh.Sexbook")
        GLib.set_application_name("Sexbook")
        self.main: Optional[Main] = None

    def do_activate(self):
        self.main = Main(self)
        self.main.present()


app = Sexbook()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
