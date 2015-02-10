#!/usr/bin/python

## This is a demo plugin for Veer. (This demo is very dull, and has limited features). ##

import pygtk
pygtk.require('2.0')
import gtk, cairo
import Veer

Frame = gtk.Frame()
buff = gtk.TextBuffer()
output = gtk.TextView(buffer=buff)
output.set_left_margin(10)
output.set_right_margin(10)
output.set_wrap_mode(gtk.WRAP_WORD_CHAR)

buff.set_text("Hello World!")

Frame.set_size_request(200, 200)
Frame.add(output)

Veer.sidebar.view.attach(Frame, 0, 1, 0, 1, gtk.EXPAND, gtk.FILL, 1, 1)
Veer.sidebar.update()

