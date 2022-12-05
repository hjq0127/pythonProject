"""
CP1404/CP5632
constant dictionary of about 10 colour names
"""

COLOUR_CODES = {"Bole": "#79443b", "Bone": "#e3dac9",
                "Boysenberry": "#873260", "Brandeis Blue": "#0070ff",
                "Brass": "#b5a642", "Brick Red": "#cb4154",
                "Bright Cerulean": "#1dacd6", "Bright Green": "#66ff00",
                "Bright Lavender": "#bf94e4", "Bright Lilac": "#d891ef",
                "Bright Maroon": "#c32148", "Bright Navy Blue": "#1974d2", "Bright Turquoise": "#08e8de",
                "Bright Ube": "#d19fe8", "Brilliant Rose": "#ff55a3"}

colour_name = input("Enter a colour name: ").capitalize()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")