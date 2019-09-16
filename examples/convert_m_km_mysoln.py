from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.clock import Clock
MI_TO_KM = 1.60934

class MVCDemo(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Metres to KM"
        self.root = Builder.load_file('convert_m_km_mysoln.kv')
        #Clock.schedule_interval(self.update, 1.0/60.0)
        return self.root

    def handle_changes(self, changed_value):
        temp = int(self.root.ids.user_input.text)
        if(temp + changed_value <0):
            self.root.ids.user_input.text = str(temp)
        else:
            temp += changed_value
            self.root.ids.user_input.text = str(temp)
    

        

    def handle_conversion(self, value):
        self.root.ids.converted_output.text = str(value * MI_TO_KM)

    def handle_validation(self, value):
        if (value <0):
            self.root.ids.converted_output.text = "Error Invalid Value Try Again"
        else:
            self.handle_conversion(value)


# create and start the App running
def main():
    flag = True
    while flag:
        try:
            MVCDemo().run()
            flag = False
        except ValueError:
            print("App Error Try Again")

if __name__ == "__main__":
    main()