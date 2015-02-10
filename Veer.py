#!/usr/bin/python

import pygtk; pygtk.require('2.0')
import gtk, cairo

class sidebar(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_decorated(False)
        self.set_app_paintable(True)
        
        self.screen = self.get_screen()
        rgba = self.screen.get_rgba_colormap()
        self.set_colormap(rgba)
    
        self.set_vwidth(self.screen.get_height() / 4)
        self.set_vheight(self.screen.get_height())
        
        self.set_size_request(20, self.get_vheight())
        self.resize(self.get_vwidth(), self.get_vheight())
        self.move(self.screen.get_width() - self.get_vwidth(), 25)

        self.view = gtk.Table(rows=self.get_vwidth(), columns=1, homogeneous=False)
        self.add(self.view)

        self.connect('expose-event', self.expose)
        self.connect('enter-notify-event', self.mouse_enter)
        self.connect('leave-notify-event', self.mouse_leave)

        self.update()

    def expose(self, widget, event):
        cr = widget.window.cairo_create()

        cr.set_operator(cairo.OPERATOR_CLEAR)
        cr.rectangle(0.0, 0.0, *widget.get_size())
        cr.fill()
        cr.set_operator(cairo.OPERATOR_OVER)

        cr.set_source_rgba(0.2, 0.2, 0.2, 0.575)
        cr.rectangle(0, 0, widget.get_vwidth(), widget.get_vheight())
        cr.fill()

    def mouse_enter(self, widget, event):
        self.resize(self.get_vwidth(), self.get_vheight())
        self.move(widget.screen.get_width() - self.get_vwidth(), 25)

    def mouse_leave(self, widget, event):
        self.resize(20, self.get_vheight())
        self.move(widget.screen.get_width() - 20, 25)
    
    def set_vwidth(self, w):
        self.vwidth = w

    def get_vwidth(self):
        return self.vwidth
    
    def set_vheight(self, h):
        self.vheight = h

    def get_vheight(self):
        return self.vheight

    def update(self):
        self.show_all()

sidebar = sidebar()
def main():
    gtk.main()
    
