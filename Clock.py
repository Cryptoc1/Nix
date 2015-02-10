#!/usr/bin/python

## This is a demo plugin for Veer. ##

import pygtk; pygtk.require('2.0')
import gtk, cairo
import Veer
import time

class Clock:
    def __init__(self):
        Frame = gtk.Frame()
        self.label = gtk.Label()
        Frame.add(self.label)
        Frame.set_border_width(10)
        Veer.sidebar.size_plugin(Frame)
        Veer.sidebar.view.attach(Frame, 1, 2, 1, 2, gtk.EXPAND, gtk.FILL, 1, 1)

    def update(self):
        hour = int(time.strftime("%H"))
        if hour > 12:
            hour = str(hour - 12)
        self.label.set_text(time.strftime(hour + " : %M"))
        return True

clock = Clock()

gtk.timeout_add(200, clock.update)

Veer.sidebar.update()
