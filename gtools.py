# File: gtools.py

"""
This module exports a library of three graphics functions
(createFilledRect, createFilledCircle, and createCenteredLabel)
that are used in several different applications.  Each of these
functions is described in its docstring comment.
"""

from pgl import GRect, GOval, GLabel

def create_filled_rect(x, y, width, height, fill="Black", border=None):
    """
    Creates a GRect filled with the specified fill color.  If border is
    specified, the border appears in that color.
    """
    rect = GRect(x, y, width, height)
    rect.set_filled(True)
    if border is None:
        rect.set_color(fill)
    else:
        rect.set_color(border)
        rect.set_fill_color(fill)
    return rect

def create_filled_circle(x, y, r, fill="Black", border=None):
    """
    Creates a circle of radius r centered at the point (x, y) with the
    specified fill color.  If border is specified, the border appears
    in that color.
    """
    circle = GOval(x - r, y - r, 2 * r, 2 * r)
    circle.set_filled(True)
    if border is None:
        circle.set_color(fill)
    else:
        circle.set_color(border)
        circle.set_fill_color(fill)
    return circle

def create_centered_label(text, x, y, font=None):
    """
    Creates a new GLabel centered at the point (x, y) in both the
    horizontal and vertical directions.  If font is specified, it
    is used to set the font of the label.
    """
    label = GLabel(text)
    if font is not None:
        label.set_font(font)
    label.set_location(x - label.get_width() / 2, y + label.get_ascent() / 2)
    return label
