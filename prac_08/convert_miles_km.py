from kivy.app import App
from kivy.lang import Builder

__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root


MilesConverterApp().run()