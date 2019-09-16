from kivy.app import App
from kivy.lang import Builder

#IMPORT AND MODIFIED FROM WEEK 3 PRACTICAL
from broken_score import fixed_solution as grade_checker 

class GradeChecker(App):
    def build(self):
        self.title = "Grade Checker"
        self.root = Builder.load_file('grade_checker.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.name_input.text = ''
        self.root.ids.output_label.text = ''

    def handle_check(self, value):
        outcome = grade_checker(value)
        self.root.ids.output_label.text = outcome

    def handle_greet(self, name):
        print("test")
        self.root.ids.output_label.text = "Hello, " + name

GradeChecker().run()