#!/usr/bin/python

import pygtk; pygtk.require('2.0')
import gtk, cairo
import importlib
import Veer

def load_plugins():
    plugins = open('Plugins.conf', 'r')
    for line in plugins.readlines():
        line = line.replace('\n', '')
        importlib.import_module(line)
    plugins.close()

def main():
    load_plugins()
    Veer.main()

if __name__ == "__main__":
   main()
