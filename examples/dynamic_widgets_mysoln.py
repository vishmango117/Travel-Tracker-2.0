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
            self.dictionary = {}

    def build(self):
            """Build the Kivy GUI."""
            self.title = "Dynamic Widgets"
            self.root = Builder.load_file('dynamic_widgets_mysoln.kv')
            return self.root
    
    def build_object(self):
        def load_places(self, filename):
        """ load_places(): FUNCTION DESIGNED TO READ CSV FILES
        AND SET THEM INTO DICTIONARY
        SORTING IS DONE BASED ON THE LIST INSIDE DICTIONARY
        PARAMS: FILENAME(STRING)
        RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

        # START OF FUNCTION
        # OPEN FILE
        try:
            file_read = open(filename, 'r')
        except FileNotFoundError:
            print("File Not Found")
            exit()
        file_row = csv.reader(file_read, delimiter=',')
        
        for data in file_row:
            #print(data[0], data[1], data[2])
            self.collection.append(Places(data[0],data[1],data[2], data[3]))
            self.collection[self.size].priority = int(self.collection[self.size].priority)
            self.create_widgets("Lima", "Peru", 12)
            self.size+=1
        file_read.close()
        self.create_widgets("Lima", "Peru", 12)


    def create_widgets(self, name, country, priority):
        """Create buttons from dictionary entries and add them to the GUI."""
        # create a button for each data entry, specifying the text and id
        # (although text and id are the same in this case, you should see how this works)
        temp_button = Button(text="{} in {}, priortity {}".format(name, country, priority), id=name+"_"+country)
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