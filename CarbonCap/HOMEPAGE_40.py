from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

Window.clearcolor = (1, 0.9569, 0.7843, 1)
Config.set('graphics', 'resizable', False)
Window.size = (1200,700)

class Button(Button):
    from quiz_final4 import QuizApp
    def __init__(self, image_file, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = None
        self.width = 500
        self.height = 90
        self.background_normal = image_file
        self.background_down = "images/brown.png"
        if "images/1.png" in image_file:
            self.bind(on_press=lambda instance: self.launch_prediction())
        if "images/2.png" in image_file:
            self.bind(on_press=lambda instance: self.launch_advice())
        if "images/3.png" in image_file:
            self.bind(on_press=lambda instance: self.launch_quiz())
        if "images/4.png" in image_file:
            self.bind(on_press=lambda instance: self.launch_controls())

    def launch_quiz(self):
        from quiz_final4 import QuizApp
        outer_layout = self.parent.parent
        for widget in outer_layout.children:
            outer_layout.remove_widget(widget)
        root_widget = App.get_running_app().root
        for widget in root_widget.walk(restrict=True):
            root_widget.remove_widget(widget)
        QuizApp().run()

    def launch_prediction(self):
        from PredictionApp import preds
        outer_layout = self.parent.parent
        for widget in outer_layout.children:
            outer_layout.remove_widget(widget)
        root_widget = App.get_running_app().root
        for widget in root_widget.walk(restrict=True):
            root_widget.remove_widget(widget)
        preds()
        

    def launch_advice(self):
        from AdviceApp import EnergySaverApp
        outer_layout = self.parent.parent
        for widget in outer_layout.children:
            outer_layout.remove_widget(widget)
        root_widget = App.get_running_app().root
        for widget in root_widget.walk(restrict=True):
            root_widget.remove_widget(widget)
        EnergySaverApp().run()

    def launch_controls(self):
        from Controls import control
        outer_layout = self.parent.parent
        for widget in outer_layout.children:
            outer_layout.remove_widget(widget)
        root_widget = App.get_running_app().root
        for widget in root_widget.walk(restrict=True):
            root_widget.remove_widget(widget)
        control().run()

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=50, padding=[40, 300, 800, 40])
        for i in range(4):
            button = Button(image_file=f"images/{i + 1}.png", text='')
            layout.add_widget(button)
        outer_layout = FloatLayout(size=(800, 600))
        image2 = Image(source='images/backround.png', size_hint=(None, None), size=(1200, 1750))
        screen_width, screen_height = Window.size
        title_banner = Image(source='images/Carbon.png', size_hint=(None, None), size=(1950, 1420), pos=(500, 500))
        outer_layout.add_widget(title_banner)
        house = Image(source='images/house2.png', size_hint=(None, None), size=(1250, 1100), pos=(800, 20))
        outer_layout.add_widget(house)
        image = Image(source='images/Menu3.png', size_hint=(None, None), size=(550, 1350), pos=(20, 20))
        outer_layout.add_widget(image)
        outer_layout.add_widget(layout)
        return outer_layout


if __name__ == '__main__':
    MainApp().run()
