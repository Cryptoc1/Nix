#!/usr/bin/python

## This is a demo plugin for Veer. (This demo is very dull, and has limited features). ##

import pygtk
pygtk.require('2.0')
import gtk, cairo
import Veer

# Plugins begin as Gtk Frames
Frame = gtk.Frame()
Frame.set_border_width(10)

# Because this is going to be a simple notepad, we'll need textviews and buffers,
# all of which are supplied by Gtk.
buff = gtk.TextBuffer()
output = gtk.TextView(buffer=buff)
output.set_left_margin(10)
output.set_right_margin(10)
output.set_wrap_mode(gtk.WRAP_WORD_CHAR)

# This is the default text on startup, like placeholder
buff.set_text("Hello World!")

# Set the size of the frame to the Sidebar's view constraints.
Veer.sidebar.size_plugin(Frame)

# Put our TextView into the plugin Frame
Frame.add(output)

# Attach the Plugin Frame to the Sidebar's 'view'.
Veer.sidebar.view.attach(Frame, 0, 1, 0, 1, gtk.EXPAND, gtk.FILL, 1, 1)

# After attaching our plugin, we need to refresh the sidebars view.
Veer.sidebar.update()

