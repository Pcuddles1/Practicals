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
        self.message = str(float(self.root.ids.user_input.text)*1.609)
    def handle_increment(self, change):
        self.root.ids.user_input.text = str(float(self.root.ids.user_input.text) + change)
        self.convert_miles()

ConvertDistanceApp().run()