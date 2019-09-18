from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import StringProperty

from PlaceCollection import PlaceCollection


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text1 = StringProperty()
    status_text2 = StringProperty()

    
    def __init__(self):
        """Construct main app."""
        super().__init__()
        self.travel_tracker = PlaceCollection()

    def on_start(self):
        self.travel_tracker.load_places("places.csv")
        for i in range(self.travel_tracker.size):
            self.create_widgets(self.travel_tracker.collection[i].name, self.travel_tracker.collection[i].country, self.travel_tracker.collection[i].priority)
        self.status_text1 = self.send_unvisited()
        self.status_text2 = "Welcome to Travel Tracker 2.0 Vishal"
        #self.send_unvisited()

    def on_stop(self):
        self.travel_tracker.save_places("places.csv")
        print("Goodbye")

    def build(self):
            """Build the Kivy GUI."""
            self.title = "Dynamic Widgets"
            self.root = Builder.load_file('app_gui_layout.kv')
            return self.root

    def create_widgets(self, name, country, priority):
        """Create buttons from dictionary entries and add them to the GUI."""
        # create a button for each data entry, specifying the text and id
        # (although text and id are the same in this case, you should see how this works)
        temp_button = Button(text="{} in {}, priortity {}".format(name, country, priority), id=name)
        # add the button to the "entries_box" layout widget
        self.root.ids.entries_box.add_widget(temp_button)

    def handle_submission(self):
        name = self.root.ids.place_input.text
        country = self.root.ids.country_input.text
        priority = int(self.root.ids.priority_input.text)
        self.create_widgets(name, country, priority)
        self.travel_tracker.add_place(name, country, priority)
        self.clear_all_entries()
        self.travel_tracker.unvisited_counter +=1
        self.status_text1 = self.send_unvisited()
        #if(self.handle_string_validation(name) == False):
        #    self.handle_clear_place()
        


    def handle_string_validation(self, value):
        if(value == ''):
            self.root.ids.diagnostic_message.text = "Input cannot be blank"
            return False
        elif(not(value.isalpha())):
            self.root.ids.diagnostic_message.text = "Invalid Name Try Again"
            return False
        return True

    def handle_clear_place(self):
        self.root.ids.place_input.text = ""
    
    def clear_all_entries(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.place_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
    
    def send_unvisited(self):
       return "Places to visit: {}".format(self.travel_tracker.get_unvisited())
