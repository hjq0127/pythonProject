from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty

NEW_COLOUR = (0, 0, 0.34, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (0, 0, 0.67, 1)  # RGBA for magenta


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name = {"Jim", "Ferris", "Bobby", "Tan", "Hu", "Harris"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name:
            # create a button for each data entry, specifying the text
            temp_button = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicWidgetsApp().run()
