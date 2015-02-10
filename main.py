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

        self.set_default_size(250, self.screen.get_height())
        self.set_size_request(250, self.screen.get_height())
        # self.set_resizable(False)

        self.move(self.screen.get_width() - 250, 20)

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
        cr.rectangle(0,0, 250, widget.screen.get_height())
        cr.fill()

    def mouse_enter(self, widget, event):
        self.set_size_request(250, self.screen.get_height())
        self.move(self.screen.get_width() - 250, 20)

    def mouse_leave(self, widget, event):
        self.set_size_request(20, self.screen.get_height())
        self.move(self.screen.get_width() - 20, 20)

    def update(self):
        self.show_all()

if __name__ == "__main__":
   sidebar()
   gtk.main()
