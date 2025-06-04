import sys

from gi.repository import GLib

from sexbook import Sexbook


# noinspection PyUnusedLocal
def custom_log_writer(log_domain, log_level, fields, message):
    if message is not None and "Vulkan" in message:
        return GLib.LogWriterOutput.HANDLED
    return GLib.LogWriterOutput.UNHANDLED


# noinspection PyArgumentList
GLib.log_set_writer_func(custom_log_writer, None)

sys.exit(Sexbook().run(sys.argv))
