# File: Enigma.py

"""
This module is the main program for the Enigma machine.  You should
not need to change this file unless you are implementing extensions.
"""

from pgl import GWindow
from EnigmaMachine import EnigmaMachine
from EnigmaConstants import ENIGMA_WIDTH, ENIGMA_HEIGHT

# Main program

def enigma():

    def mousedown_action(e):
        gobj = gw.get_element_at(e.get_x(), e.get_y())
        if gobj is not None:
            if getattr(gobj, "mousedown_action", None) is not None:
                gobj.mousedown_action(enigma)

    def mouseup_action(e):
        gobj = gw.get_element_at(e.get_x(), e.get_y())
        if gobj is not None:
            if getattr(gobj, "mouseup_action", None) is not None:
                gobj.mouseup_action(enigma)

    def click_action(e):
        gobj = gw.get_element_at(e.get_x(), e.get_y())
        if gobj is not None:
            if getattr(gobj, "click_action", None) is not None:
                gobj.click_action(enigma)

    gw = GWindow(ENIGMA_WIDTH, ENIGMA_HEIGHT)
    enigma = EnigmaMachine(gw)
    gw.add_event_listener("mousedown", mousedown_action)
    gw.add_event_listener("mouseup", mouseup_action)
    gw.add_event_listener("click", click_action)

# Startup code

if __name__ == "__main__":
    enigma()
