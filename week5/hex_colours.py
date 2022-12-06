"""
CP1404/CP5632
constant dictionary of about 10 colour names
"""

COLOUR_CODES = {
    "Aliceblue": "#f0f8ff",
    "Beige": "#f5f5dc",
    "Cadetblue": "#5f9ea0",
    "Darkslategrey": "#2f4f4f",
    "Hotpink": "#ff69b4",
    "Lavender": "#e6e6fa",
    "Lightcoral": "#f08080",
    "Mediumaquamarine": "#66cdaa",
    "Olivedrab": "#6b8e23",
    "Tomato": "#ff6347"
}

colour_name = input("Enter a colour name: ").capitalize()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")