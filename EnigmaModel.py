######################################################################
# Name:
# Who did you work with (if anyone):
# GenAI transcript (if used):
# Section leader's name:
# List of extensions made (if any):
######################################################################

""" This is the starter file for the Enigma project. """

from EnigmaView import EnigmaView

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return False        # In the starter version, keys are all up

    def is_lamp_on(self, letter):
        return False        # In the starter version, lamps are all off

    def key_pressed(self, letter):
        # You need to fill in this code, but leave the update call
        self.update()

    def key_released(self, letter):
        # You need to fill in this code, but leave the update call
        self.update()

    def get_rotor_letter(self, index):
        return "A"          # In the starter version, all rotors are set to "A"

    def rotor_clicked(self, index):
        # You need to fill in this code, but leave the update call
        self.update()


def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
