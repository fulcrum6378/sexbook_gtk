import sys

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk


class Sexbook(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="ir.mahdiparastesh.Sexbook")
        GLib.set_application_name("Sexbook")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Sexbook")
        window.present()


app = Sexbook()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
