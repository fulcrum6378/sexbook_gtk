import os
import sys
from typing import Optional

import gi

from main import Main

gi.require_version("Gtk", "4.0")
from gi.repository import Gdk, GLib, Gtk


class Sexbook(Gtk.Application):
    """
    :ivar main: the `Main` window
    """

    def __init__(self):
        super().__init__(application_id="ir.mahdiparastesh.Sexbook")
        GLib.set_application_name("Sexbook")
        self.main: Optional[Main] = None

    def do_activate(self):
        # launch Main
        self.main = Main(self)
        self.main.present()

        # load CSS
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(os.path.join(os.path.dirname(__file__), "style.css"))
        # noinspection PyArgumentList
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


sys.exit(Sexbook().run(sys.argv))
