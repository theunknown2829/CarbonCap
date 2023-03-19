from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.config import Config
from kivy.core.window import Window



Window.clearcolor = (0.2824, 0.7961,0.8863, 1)
Window.size = (1200,700)

class Personality2(App):
    def build(self): 
        root = Scatter(do_scale=False)
        bg_image = Image(source='images/pers2.png', size_hint=(1, 1),size=(2000, 1500))
        root.add_widget(bg_image)
        home_button = Image(source='images/home.png', size_hint=(None, None), size=(400, 400), pos=(1950, 80))
        home_button.bind(on_touch_down=self.home)
        root.add_widget(home_button)
        return root

    def home(self, instance, touch):
        from HOMEPAGE_40 import MainApp
        if instance.collide_point(*touch.pos):
            root_widget = App.get_running_app().root
            for widget in root_widget.walk(restrict=True):
                root_widget.remove_widget(widget)
            main_app = MainApp()
            main_app.run()

if __name__ == '__main__':
    Personality2().run()
