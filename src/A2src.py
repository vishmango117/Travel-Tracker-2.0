from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.clock import Clock
from kivy.uix.button import Button

MI_TO_KM = 1.60934

class MVCDemo(App):
    message = StringProperty()



    def build(self):
        self.title = "Travel Tracker 2.0"
        self.root = Builder.load_file('layout.kv')
        #Clock.schedule_interval(self.update, 1.0/60.0)
        return self.root

    
    def handle_submission(self):

        if(self.handle_string_validation(self.root.ids.name_input.text)):
            self.handle_clear_name()
            return False
        else:
            name = self.root.ids.name_input.text
        if(self.handle_string_validation(self.root.ids.name_input.text)):
            self.handle_clear_country()
            return False
        else:
            country = self.root.ids.name_input.text
        if(self.handle_string_validation(self.root.ids.name_input.text)):
            self.handle_clear_priority()
            return False
        else:
            priority = self.root.ids.name_input.text
        
        self.create_widgets(name, country, priority)
        return True
    
    
    def create_widgets(self, name, country, priority):
        """Create buttons from dictionary entries and add them to the GUI."""
        # create a button for each data entry, specifying the text and id
        # (although text and id are the same in this case, you should see how this works)
        temp_button = Button(text="{} in {}, priority {}".format(name, country, priority), id=name)
        temp_button.bind(on_release=self.press_entry)
        # add the button to the "entries_box" layout widget
        self.root.ids.dictionary_display.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handle pressing entry buttons.
        :param instance: the Kivy button instance that was clicked
        """
        # get name (dictionary key) from the id of Button we clicked on
        name = instance.id  # or name = instance.text
        # update status text
        self.status_text = "lol"
        

    def handle_string_validation(self, value):
        if(value == ''):
            print("Input cannot be blank")
            return False
        elif(not(value.isalpha())):
            print("Invalid Country Try Again")
            return False
        else:
            return True
    
    def handle_int_validation(self, value):
            try:
                if(value <= 0):
                    self.root.ids.diagonstic_message.text = "Number must be > 0"
                    return False
                else:
                    return True
            except ValueError:
                self.root.ids.diagonstic_message.text = "Invalid input; enter a valid number"
                return False
    
    def handle_clear_priority(self):
        self.root.ids.priority_input.text = ""

    def handle_clear_country(self):
        self.root.ids.country_input.text = ""
    
    def handle_clear_name(self):
        self.root.ids.place_input.text = ""


        

# create and start the App running