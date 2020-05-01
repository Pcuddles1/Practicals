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
        valid = self.check_valid()
        self.message = str(valid*1.609)
    def handle_increment(self, change):
        valid = self.check_valid() + change
        self.root.ids.user_input.text = str(valid)
        self.convert_miles()
    def check_valid(self):
        try:
            valid = float(self.root.ids.user_input.text)
            return valid
        except ValueError:
            return 0


ConvertDistanceApp().run()