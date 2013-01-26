#!/usr/bin/env python 
import gobject
import gtk
import appindicator
from subprocess import call

class BrightnessValue:
  def __init__(self, name, value, profile):
    self.name = name
    self.value = value
    self.profile = profile
 
def menuitem_response(w, bv):
  change_colour_profile(bv.profile)
  change_brightness(bv.value)

def change_colour_profile(profile):
  call (["colormgr", "device-make-profile-default",
	"/org/freedesktop/ColorManager/devices/xrandr_Hewlett_Packard_HP_LP2475w_CZC91101CT_timothy_1000",
	"%s" % profile])

def change_brightness(preset):
  call(["/home/timothy/src/ddccontrol/src/ddccontrol/ddccontrol",
	"-p",
	"-r","0x10",
	"-w","%d" % preset])

def add_menu_item(menu, bv):
    menu_items = gtk.MenuItem(bv.name)
    menu.append(menu_items)
    menu_items.connect("activate", menuitem_response, bv)
    menu_items.show()
 
if __name__ == "__main__":

  ind = appindicator.Indicator ("brightness-color-control",
                              "display-brightness-symbolic",
                              appindicator.CATEGORY_APPLICATION_STATUS)
  ind.set_status (appindicator.STATUS_ACTIVE)
 
  # create a menu
  menu = gtk.Menu()
  add_menu_item(menu, BrightnessValue("0% Brightness", 0, "/org/freedesktop/ColorManager/profiles/icc_9d0dfb5437819a5e8b028cff1f56e30a"))
  add_menu_item(menu, BrightnessValue("100% Brightness", 100, "/org/freedesktop/ColorManager/profiles/icc_6d1e1607185fb20644a53e574add89e7_timothy_1000"))
  ind.set_menu(menu)
  gtk.main()
