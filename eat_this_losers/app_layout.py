# Kivy Libraries
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import StringProperty

# Other System Libraries
from operator import attrgetter

# Importing Classes
from PlaceCollection import PlaceCollection
from Places import Place


class TravelTrackerApp(App):
    """Main Class - Kivy app to the Travel Tracker App"""

    # String Properties setup for the unvisited display counter on top
    # and Program Status bar at the bottom,
    unvisited_display = StringProperty()
    program_message = StringProperty()

    def __init__(self, my_placecollection_obj):
        """__init__() : Method that loads the TravelTrackerApp on load"""

        super().__init__()
        self.travel_tracker = my_placecollection_obj

    def on_start(self):
        """on_start(): Method that tells the interpreter
         what to load first before loading tht GUI Window.
        In this case we set it to load the list object from the file
        and send the unvisited display and program status message."""

        self.travel_tracker.load_places("places.csv")
        for i in range(self.travel_tracker.size):
            self.create_widgets(self.travel_tracker.collection[i])
        self.unvisited_display = self.send_unvisited()
        self.program_message = "Welcome to Travel Tracker 2.0 Vishal"

    def on_stop(self):
        """on_stop(): Method that tells the interpreter
        to execute this method before terminating the program.
        In this case we override the method to """

        self.travel_tracker.save_places("places.csv")
        print("Program Terminated")

    def build(self):
            """Build(): Method to build the Kivy GUI.
            Invokes the on_start() function before loading the Window"""
            self.title = "Dynamic Widgets"
            self.root = Builder.load_file('app_gui_layout.kv')
            return self.root

    def create_widgets(self, placeobj):
        """Create buttons from list of  entries and add them to the GUI."""

        # choosing based on visited and unvisited which will create the button
        # with different background colors
        if(placeobj.visited == "v"):
            temp_button = Button(text=placeobj.__str__(), id=placeobj.name,
                                 background_normal='',
                                 background_color=[0, 0, 0, 0])
        else:
            temp_button = Button(text=placeobj.__str__(), id=placeobj.name,
                                 background_normal='',
                                 background_color=[0.027, 0.212, 0.259, 1])
        temp_button.bind(on_press=self.handle_visit)
        # add the button to the "entries_box" layout widget
        self.root.ids.entries_box.add_widget(temp_button)

    def handle_visit(self, instance):

        button_name = instance.id
        for i in range(self.travel_tracker.size):
            if(self.travel_tracker.collection[i].name == button_name):
                if(self.travel_tracker.collection[i].visited == "n"):
                    self.travel_tracker.collection[i].mark_visited()
                    self.travel_tracker.unvisited_counter -= 1

                    if(self.travel_tracker.collection[i].important_place()):
                        self.program_message = "You visited {}."
                        "Great Travelling".format(button_name)
                    else:
                        self.program_message = "You visited {}"
                        .format(button_name)
                else:
                    self.travel_tracker.collection[i].mark_unvisited()
                    self.travel_tracker.unvisited_counter += 1
                    if(self.travel_tracker.collection[i].important_place()):
                        self.program_message = "You need to visit {}."
                        " Get Going!".format(button_name)
                    else:
                        self.program_message = "You need to visit {}"
                        .format(button_name)

                instance.text = self.travel_tracker.collection[i].__str__()
        self.unvisited_display = self.send_unvisited()

        self.travel_tracker.collection.sort(
            key=attrgetter("visited", "priority"))

        self.root.ids.entries_box.clear_widgets()
        for i in range(self.travel_tracker.size):
            self.create_widgets(self.travel_tracker.collection[i])

    def handle_sort_option(self, option):
        if(option == "Visited"):
            self.travel_tracker.collection.sort(
                key=attrgetter("visited", "priority"))
            self.root.ids.entries_box.clear_widgets()
            for i in range(self.travel_tracker.size):
                self.create_widgets(self.travel_tracker.collection[i])

        elif(option == "Country"):
            self.travel_tracker.collection.sort(
                key=attrgetter("country", "priority"))
            self.root.ids.entries_box.clear_widgets()
            for i in range(self.travel_tracker.size):
                self.create_widgets(self.travel_tracker.collection[i])

        elif(option == "City"):
            self.travel_tracker.collection.sort(
                key=attrgetter("name", "priority"))
            self.root.ids.entries_box.clear_widgets()
            for i in range(self.travel_tracker.size):
                self.create_widgets(self.travel_tracker.collection[i])

        else:
            self.travel_tracker.collection.sort(
                key=attrgetter("visited", "priority"))
            self.root.ids.entries_box.clear_widgets()
            for i in range(self.travel_tracker.size):
                self.create_widgets(self.travel_tracker.collection[i])

    def handle_submission(self):
        if(self.handle_string_validation(
                self.root.ids.place_input.text, "Place") and
           self.handle_string_validation(
                self.root.ids.country_input.text, "Country") and
           self.handle_int_validation(
                self.root.ids.priority_input.text, "Priority")):

            name = self.root.ids.place_input.text
            country = self.root.ids.country_input.text
            priority = int(self.root.ids.priority_input.text)
            self.create_widgets(Place(name, country, priority))
            self.travel_tracker.add_place(name, country, priority)
            self.unvisited_display = self.send_unvisited()
            self.clear_all_entries()

    def handle_string_validation(self, value, variable_name):
        if(value == ''):
            self.program_message = "All fields must be completed"
            return False
        elif(not(value.isalpha())):
            self.program_message = "Invalid {} Try Again".format(variable_name)
            return False
        return True

    def handle_int_validation(self, value, variable_name):
        try:
            if(value == ''):
                self.program_message = "All fields must be completed"
            else:
                value = int(value)
                if(value <= 0):
                    self.program_message = "{} must be > 0"
                    .format(variable_name)
                    return False
                else:
                    return True
        except ValueError:
            self.program_message = "Please enter a valid number"
            return False

    def handle_clear_place(self):
        self.root.ids.place_input.text = ""

    def handle_clear_country(self):
        self.root.ids.country_input.text = ""

    def handle_clear_priority(self):
        self.root.ids.priority_input.text = ""

    def clear_all_entries(self):
        """Clear_all_entries(): Methods to clear the
        name_input, country_input, priority_input and status bar."""
        self.handle_clear_place()
        self.handle_clear_country()
        self.handle_clear_priority()
        self.program_message = ""

    def send_unvisited(self):
        return "Places to visit: {}".format(
            self.travel_tracker.get_unvisited())
