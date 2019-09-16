from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
            """Construct main app."""
            super().__init__(**kwargs)
            # basic data example - dictionary of names: phone numbers
            # TODO: After running it, add another entry to the dictionary and see how the layout changes
            self.dictionary = {}

    def build(self):
            """Build the Kivy GUI."""
            self.title = "Dynamic Widgets"
            self.root = Builder.load_file('dynamic_widgets_mysoln.kv')
            return self.root
    
    def build_object(self):
        name = input("Enter Name: ")
        number = int(input("Enter Number: "))
        self.create_widgets(number, name)
        self.dictionary[name] = number


    def create_widgets(self, number, name):
        """Create buttons from dictionary entries and add them to the GUI."""
        # create a button for each data entry, specifying the text and id
        # (although text and id are the same in this case, you should see how this works)
        temp_button = Button(text=name, id=name)
        temp_button.bind(on_release=self.press_entry)
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


DynamicWidgetsApp().run()