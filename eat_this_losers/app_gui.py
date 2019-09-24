"""CP1404 Programming-II Assignment-2 Travel Tracker 2.0
app_gui.py: Main program for all the gui build
and running the main functions of application window itself
consists of unvisited_display and program_message as StringProperty()
and methods like create_widgets, handle_visit, handle_sort_option(),
handle_string_validation(), handle_submission(), handle_int_validation() and
clear_all_entries()"""

# Kivy Libraries
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import StringProperty

# Other System Libraries
from operator import attrgetter

# Importing Classes
# from PlaceCollection import PlaceCollection
# from Places import Place


class TravelTrackerApp(App):

    # Variables to display program message or counter for unvisited places.
    unvisited_display = StringProperty()
    program_message = StringProperty()


    def __init__(self, my_placecollection_obj):
        """__init__() : Method that loads the TravelTrackerApp on load
        calls the super classes __init__  function and sets the object."""
        super().__init__()
        self.travel_tracker = my_placecollection_obj

    def on_start(self):
        """on_start(): Method that is called before the application is running
        and is called right after the build method. In this case we
        from the file
        and send the unvisited display and program status message."""

        self.travel_tracker.load_places("places.csv")
        for i in range(self.travel_tracker.size):
            self.create_widgets(self.travel_tracker.collection[i])
        self.unvisited_display = self.send_unvisited()
        self.program_message = "Welcome to Travel Tracker 2.0 Vishal"

    def on_stop(self):
        """on_stop(): Method that is executed before terminating the window.
        In this case we the override the method to save the places
        when the program is exited."""

        self.travel_tracker.save_places("places.csv")
        print("Program Terminated")

    def build(self):
        """Build(): Method to build the Kivy GUI.
        Invokes the on_start() function before loading the Window"""

        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('app_gui_layout.kv')
        return self.root

    def create_widgets(self, placeobj):
        """Create buttons from dictionary entries and add them to the GUI."""
        # create a button for each data entry, specifying the text and id
        # (although text and id are the same in this case, you should see how this works)
        if(placeobj.visited == "v"):
            temp_button = Button(text=placeobj.__str__(), id=placeobj.name,
            background_normal = '', background_color= [0,0,0,0])
        else:
            temp_button = Button(text=placeobj.__str__(), id=placeobj.name,
            background_normal = '', background_color= [0.027, 0.212, 0.259, 1])
        temp_button.bind(on_press = self.handle_visit)
        # add the button to the "entries_box" layout widget
        self.root.ids.entries_box.add_widget(temp_button)

    def handle_visit(self, instance):
        """handle_visit(): Handles on what to do if button on the place is pressed
        in this case it will check whether update the dictionary
        is either to be visited or unvisited by which
        it will sort based on the new value
        and update the GUI based on the new values"""

        button_name = instance.id
        for i in range (self.travel_tracker.size):
            if(self.travel_tracker.collection[i].name == button_name):
                if(self.travel_tracker.collection[i].visited == "n"):
                    self.travel_tracker.collection[i].mark_visited()
                    self.travel_tracker.unvisited_counter -= 1

                    if(self.travel_tracker.collection[i].important_place()):
                        self.program_message = "You visited {}. Great Travelling".format(button_name)
                    else:
                        self.program_message = "You visited {}".format(button_name)
                else:
                    self.travel_tracker.collection[i].mark_unvisited()
                    self.travel_tracker.unvisited_counter += 1
                    if(self.travel_tracker.collection[i].important_place()):
                        self.program_message = "You need to visit {} Get Going!".format(button_name)
                    else:
                        self.program_message = "You need to visit {}".format(button_name)

                instance.text = self.travel_tracker.collection[i].__str__()
        self.unvisited_display = self.send_unvisited()
        self.travel_tracker.collection.sort(key=attrgetter("visited", "priority"))
        self.root.ids.entries_box.clear_widgets()
        for i in range(self.travel_tracker.size):
            self.create_widgets(self.travel_tracker.collection[i])

    def handle_sort_option(self, option):
        """handle_sort_option(): Method to execute when the GUI app spinner menu is chosen
        based on the selection the sort function is called based on a combination of
        1. Visited and Priority 2. Country and Priority 3. City and Priority """
        #Set sorting based on the option set by the spinner in the kv

        # Option is Visited
        if(option == "Visited"):
            self.travel_tracker.collection.sort(key=attrgetter("visited", "priority"))
            self.root.ids.entries_box.clear_widgets()
            for i in range(self.travel_tracker.size):
                self.create_widgets(self.travel_tracker.collection[i])

        # Option is Country
        elif(option == "Country"):
            self.travel_tracker.collection.sort(key=attrgetter("country", "priority"))
            self.root.ids.entries_box.clear_widgets()
            for i in range(self.travel_tracker.size):
                self.create_widgets(self.travel_tracker.collection[i])
            
        # Option is City
        elif(option == "City"):
            self.travel_tracker.collection.sort(key=attrgetter("name", "priority"))
            self.root.ids.entries_box.clear_widgets()
            for i in range(self.travel_tracker.size):
                self.create_widgets(self.travel_tracker.collection[i])


    def handle_submission(self):
        """handle_submission(): Method to execute when the Add Place button is pressed
        It will do the error checks on inputs of name, country, priority
        and based on input it will either print the appropriate error message
        or it will add the place to the list
        alongside with create the widget for the new place."""

        name = self.root.ids.place_input.text
        country = self.root.ids.country_input.text
        priority = self.root.ids.priority_input.text
        if(self.handle_string_validation(name, "Place") and
           self.handle_string_validation(country, "Country") and
           self.handle_int_validation(priority, "Priority")):
            priority = int(self.root.ids.priority_input.text)
            self.create_widgets(Place(name, country, priority))
            self.travel_tracker.add_place(name, country, priority)
            self.unvisited_display = self.send_unvisited()
            self.clear_all_entries()
            self.program_message = "{} in {} (priority {}) added to Travel Tracker".format(name, country, priority)
        


    def handle_string_validation(self, value, variable_name):
        """handle_string_validation(): Method to handle inputs of string types
        checks for blank strings and if characters are alphabetic"""

        if(value == ''):
            self.program_message = "All fields must be completed"
            return False
        elif(not(value.isalpha())):
            self.program_message = "Invalid {} Try Again".format(variable_name)
            return False
        return True
    
    def handle_int_validation(self, value, variable_name):
        """handle_int_validation(): Method to handle inputs of integer types
        checks whether data type is a blank value or a valid positive value."""

        try:
            if(value == ''):
                self.program_message = "All fields must be completed"
            else:
                value = int(value)
                if(value <= 0):
                    self.program_message = "{} must be > 0".format(variable_name)
                    return False
                else:
                    return True
        except ValueError:
            self.program_message = "Please enter a valid number"
            return False
    
    def clear_all_entries(self):
        """Clear_all_entries(): Method to clear entries on button press Clear
           name_input, country_input, priority_input and status bar."""
        
        # Clear all inputs
        self.root.ids.place_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
        # Clear Status Bar
        self.program_message = ""
    
    def send_unvisited(self):
       return "Places to visit: {}".format(self.travel_tracker.get_unvisited())
