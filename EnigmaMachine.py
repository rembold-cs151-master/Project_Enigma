# File: EnigmaMachine.py

"""
This module is the starter file for the EnigmaMachine class.
"""

from pgl import GImage

# Class: EnigmaMachine

class EnigmaMachine():
    """
    This class is responsible for storing the data needed to simulate
    the Enigma machine.  If you need to maintain any state information
    that must be shared among different parts of this implementation,
    you should define that information as part of this class and
    provide the necessary getters, setters, and other methods needed
    to manage that information.
    """

    def __init__(self, gw):
        """
        The constructor for the EnigmaMachine class is responsible for
        initializing the graphics window along with the state variables
        that keep track of the machine's operation.
        """
        image = GImage("images/EnigmaTopView.png")
        gw.add(image)
