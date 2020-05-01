from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty


class ConvertDistanceApp(App):
    message = StringProperty()
    def build(self):
        Window.size = (500, 200)
        self.title = "Converting Distances"
        self.root = Builder.load_file('convert_miles_km')
        return self.root
    def convert_miles(self):
        valid = self.check_value()
        self.message = str(valid*1.609)
    def handle_increment(self, change):
        valid = self.check_value() + change
        self.root.ids.user_input.text = str(value)
        self.convert_miles()
    def check_value(self):
        try:
            valid = self.root.ids.user_input.text
            return valid
        except ValueError:
            return 0


ConvertDistanceApp().run()