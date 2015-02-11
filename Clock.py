#!/usr/bin/python

## This is a demo plugin for Veer. ##

import pygtk; pygtk.require('2.0')
import gtk, cairo
import Veer
import time

# Defines the Clock Class we'll be using.
class Clock:
    def __init__(self):
        Frame = gtk.Frame()
        self.label = gtk.Label()
        Frame.add(self.label)
        Frame.set_border_width(10)

        # Size and attach the Plugin to the sidebar view
        Veer.sidebar.size_plugin(Frame)
        Veer.sidebar.view.attach(Frame, 0, 1, Veer.TOP_ATTACH, Veer.BOTTOM_ATTACH, gtk.EXPAND, gtk.FILL, 1, 1)

    def update(self):
        hour = int(time.strftime("%H"))
        if hour > 12:
            hour = str(hour - 12)
        self.label.set_text(time.strftime(hour + " : %M"))
        return True

clock = Clock()

# This keeps the updating, or 'ticking', of the clock in-sync with the Gtk loop
gtk.timeout_add(200, clock.update)

# Update the view, as always.
Veer.sidebar.update()
