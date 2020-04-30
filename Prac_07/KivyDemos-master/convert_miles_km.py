from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertDistanceApp(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Converting Distances"
        self.root = Builder.load_file('convert_miles_km')
        return self.root

ConvertDistanceApp().run()