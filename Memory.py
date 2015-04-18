#!/usr/bin/python
import pygtk; pygtk.require('2.0')
import gtk, cairo
import Veer

import re

class Graph:
    def __init__(self):
        self.DrawingArea = gtk.DrawingArea()
        self.DrawingArea.set_app_paintable(True)
        # self.DrawingArea.connect('expose-event', self.update)

        Veer.sidebar.size_plugin(self.DrawingArea)
        Veer.sidebar.view.attach(self.DrawingArea, 0, 1, Veer.TOP_ATTACH, Veer.BOTTOM_ATTACH, gtk.EXPAND, gtk.FILL, 1, 1)

    def update(self):
        cr = self.DrawingArea.window.cairo_create()

        cr.set_operator(cairo.OPERATOR_CLEAR)
        cr.rectangle(0, 0, *self.DrawingArea.window.get_size())
        cr.fill()
        cr.set_operator(cairo.OPERATOR_OVER)

        self.update_cpu_info()
        print self.cpu_proc
        cr.set_source_rgba(0.8, 0.4, 0.4, 0.65)
        cr.rectangle(0, 90, (int(self.cpu_proc) / 1000), 10)
        cr.fill()
    
    def update_cpu_info(self):
        f = open('/proc/stat', 'r')
        cpu_stat = f.readline().split()
        self.cpu_proc = cpu_stat[1]
        f.close()

    def update_mem_info(self):
        f = open('/proc/meminfo', 'r')
        mem_total = f.readline()
        mem_free = f.readline()
        mem_total = re.sub('[A-Z-a-z-:]', '', mem_total)
        self.mem_total = float(mem_total.replace(" ", ""))
        mem_free = re.sub('[A-Z-a-z-:]', '', mem_free)
        self.mem_free = float(mem_free.replace(" ", ""))
        self.mem_used = self.mem_total - self.mem_free
        self.usage = self.mem_used / self.mem_total
        f.close()

graph = Graph()

gtk.timeout_add(200, graph.update)

Veer.sidebar.update()
