#!/usr/bin/python

import pygtk; pygtk.require('2.0')
import gtk, cairo


#######                                                      #######   
###                                                              ###
### This file will be used as an API to create Plugins/Widgets   ###
### for Nix Plugin Sidebar. Created by Samuel Steele (Cryptoc1). ###
###                                                              ###       
#######                                                      #######

class Plugin(gtk.Widget):
    # TODO: Create easy-to-use plugin api

class Event(gtk.Event):
    # TODO: Create events like click, scroll, 'zoom' (CTRL + and CTRL -)
