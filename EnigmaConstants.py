# File: EnigmaConstants.py

"""
This module defines the constants used in the Enigma simulator.
"""

# The letters of the alphabet

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Constants that specify the size of the Enigma image.

ENIGMA_WIDTH = 818
ENIGMA_HEIGHT = 694

# The early German Enigma machines include three rotors, which advance
# at different speeds.  The rotor on the right is the "fast" rotor,
# which advances on every keystroke.  The rotor in the middle is the
# "medium" rotor, which advances when the fast rotor has made a
# complete revolution.  The rotor at the left is the "slow" rotor,
# which advances when the medium rotor has made a complete cycle.
# The ROTOR_PERMUTATION array lists the three rotors from left to
# right: the slow rotor, the medium rotor, and the fast rotor.
#
# Each rotor implements a letter-substitution cipher, which is
# represented by a string of 26 uppercase letters that shows how
# the letters in the alphabet are mapped to new letters as the
# internal signal flows across the rotor from right to left.  For
# example, the slow rotor corresponds to the following mapping
# when it is in its initial position:
#
#    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#    | | | | | | | | | | | | | | | | | | | | | | | | | |
#    E K M F L G D Q V Z N T O W Y H X U S P A I B R C J

ROTOR_PERMUTATIONS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Permutation for slow rotor      
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Permutation for medium rotor    
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Permutation for fast rotor      
]

# Constants that control the display of the current rotor setting 

ROTOR_BGCOLOR = "#BBAA77"       # Background color for the rotor  
ROTOR_WIDTH = 24                # Width of the setting indicator  
ROTOR_HEIGHT = 26               # Height of the setting indicator 
ROTOR_COLOR = "Black"           # Text color of the rotor         
ROTOR_LABEL_DY = 9              # Offset from center to baseline  
ROTOR_FONT = "24px 'Helvetica Neue','Arial','Sans-Serif'"

# This array specifies the coordinates of each rotor display 

ROTOR_LOCATIONS = [
    (244, 95),
    (329, 95),
    (412, 95)
]

# To the left of the slow rotor, the Enigma machine includes a
# component called the "reflector," which implements a fixed
# permutation that remains unchanged as the rotors advance.  The
# constant REFLECTOR_PERMUTATION defines the mapping of the reflector.
# Note that the reflector is symmetric.  If A is transformed to I,
# then I is transformed to A.

REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"

# Constants that define the keys on the Enigma keyboard 

KEY_RADIUS = 24                 # Outer radius of a key in pixels 
KEY_BORDER = 3                  # Width of the key border         
KEY_BORDER_COLOR = "#CCCCCC"    # Fill color of the key border    
KEY_BGCOLOR = "#666666"         # Background color of the key     
KEY_UP_COLOR = "#CCCCCC"        # Text color when the key is up   
KEY_DOWN_COLOR = "#CC3333"      # Text color when the key is down 
KEY_LABEL_DY = 10               # Offset from center to baseline  
KEY_FONT = "bold 28px 'Helvetica Neue','Arial','Sans-Serif'"

# This array determines the coordinates of a key for each letter index 

KEY_LOCATIONS = [
    (140, 566),    # A
    (471, 640),    # B
    (319, 639),    # C
    (294, 567),    # D
    (268, 495),    # E
    (371, 567),    # F
    (448, 567),    # G
    (523, 567),    # H
    (650, 496),    # I
    (598, 567),    # J
    (674, 567),    # K
    (699, 641),    # L
    (624, 641),    # M
    (547, 640),    # N
    (725, 497),    # O
    ( 92, 639),    # P
    (115, 494),    # Q
    (345, 495),    # R
    (217, 566),    # S
    (420, 496),    # T
    (574, 496),    # U
    (395, 639),    # V
    (192, 494),    # W
    (242, 639),    # X
    (168, 639),    # Y
    (497, 496)     # Z 
]

# Constants that define the lamps above the Enigma keyboard 

LAMP_RADIUS = 23                # Radius of a lamp in pixels      
LAMP_BORDER_COLOR = "#111111"   # Line color of the lamp border   
LAMP_BGCOLOR = "#333333"        # Background color of the lamp    
LAMP_OFF_COLOR = "#666666"      # Text color when the lamp is off 
LAMP_ON_COLOR = "#FFFF99"       # Text color when the lamp is on  
LAMP_LABEL_DY = 9               # Offset from center to baseline  
LAMP_FONT = "bold 24px 'Helvetica Neue','Arial','Sans-Serif'"

# This array determines the coordinates of a lamp for each letter index 

LAMP_LOCATIONS = [
    (144, 332),    # A
    (472, 403),    # B
    (321, 402),    # C
    (296, 333),    # D
    (272, 265),    # E
    (372, 333),    # F
    (448, 334),    # G
    (524, 334),    # H
    (650, 266),    # I
    (600, 335),    # J
    (676, 335),    # K
    (700, 403),    # L
    (624, 403),    # M
    (549, 403),    # N
    (725, 267),    # O
    ( 94, 401),    # P
    (121, 264),    # Q
    (347, 265),    # R
    (220, 332),    # S
    (423, 265),    # T
    (574, 266),    # U
    (397, 402),    # V
    (197, 264),    # W
    (246, 402),    # X
    (170, 401),    # Y
    (499, 265)     # Z 
]
