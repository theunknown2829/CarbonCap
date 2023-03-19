from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.config import Config
from kivy.core.window import Window



Window.clearcolor = (0.3529, 0.2196, 0.5294,1)
Window.size = (1200,700)

class Personality3(App):
    def build(self): 
        # Create the root widget
        root = Scatter(do_scale=False)

        # Add the background image to the root widget
        bg_image = Image(source='Images/pers3.png', size_hint=(1, 1),size=(2000, 1500))
        root.add_widget(bg_image)

        # Add the home button to the root widget
        home_button = Image(source='Images/home.png', size_hint=(None, None), size=(400, 400), pos=(1950, 80))
        home_button.bind(on_touch_down=self.home)
        root.add_widget(home_button)

        # Return the root widget as the top-level widget of your app
        return root

    def home(self, instance, touch):
        from HOMEPAGE_40 import MainApp
        if instance.collide_point(*touch.pos):
                 # get the root widget of the app
            root_widget = App.get_running_app().root

            # remove all widgets from the root widget
            for widget in root_widget.walk(restrict=True):
                root_widget.remove_widget(widget)
            main_app = MainApp()
            main_app.run()

if __name__ == '__main__':
    Personality3().run()
