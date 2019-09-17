from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import StringProperty

from PlaceCollection import PlaceCollection


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self):
            """Construct main app."""
            super().__init__()

    def on_start(self):
        travel_tracker = PlaceCollection()
        travel_tracker.load_places("classes\\places_base.csv")
        for i in range(travel_tracker.size):
            self.create_widgets(travel_tracker.collection[i].name, travel_tracker.collection[i].country, travel_tracker.collection[i].priority)

    def build(self):
            """Build the Kivy GUI."""
            self.title = "Dynamic Widgets"
            self.root = Builder.load_file('app_gui_layout.kv')
            self.create_widgets("Default","Country", "Priority")
            return self.root

    def create_widgets(self, name, country, priority):
        """Create buttons from dictionary entries and add them to the GUI."""
        # create a button for each data entry, specifying the text and id
        # (although text and id are the same in this case, you should see how this works)
        temp_button = Button(text="{} in {}, priortity {}".format(name, country, priority), id=name)
        # add the button to the "entries_box" layout widget
        self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handle pressing entry buttons.
        :param instance: the Kivy button instance that was clicked
        """
        # get name (dictionary key) from the id of Button we clicked on
        name = instance.id  # or name = instance.text
        # update status text
        self.status_text = "{}'s number is {}".format(name,self.dictionary[name])
    
    def clear_all(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()
