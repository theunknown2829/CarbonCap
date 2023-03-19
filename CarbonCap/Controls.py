from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window


class control(App):
    def build(self):
        title = Image(source='images/controlstitle.png', size_hint=(1,1.8), allow_stretch=True, height=300)
        layout = GridLayout(cols=5, rows=3, row_force_default=True, row_default_height=300)
        for i in range(2):
            empty_widget = Widget()
            layout.add_widget(empty_widget)

        
        layout.add_widget(title)
        for i in range(2):
            empty_widget = Widget()
            layout.add_widget(empty_widget)

        ecomodeoff = Image(source='images/ecomodeoff.png', size_hint=(1, None), allow_stretch=True, height=800)

        button_ecomode = Button(background_normal='images/ecomodeoff.png', background_down='images/ecomodeon.png')
        button_ecomode.bind(on_press=lambda x: self.change_image(button_ecomode, ecomodeoff))
        layout.add_widget(button_ecomode)

        switches = Image(source='images/switchoff.png', size_hint=(1, None), allow_stretch=False, height=800)

        button_switches = Button(background_normal='images/switcheson.png', background_down='images/switchoff.png')
        button_switches.bind(on_press=lambda x: self.change_image(button_switches, switches))
        layout.add_widget(button_switches)

        brightness = Image(source='images/brightoff.png', size_hint=(1, None), allow_stretch=False, height=800)

        button_brightness = Button(background_normal='images/brightoff.png', background_down='images/brighton.png')
        button_brightness.bind(on_press=lambda x: self.change_image(button_brightness, brightness))
        layout.add_widget(button_brightness)

        showcurrentenergydata = Image(source='images/showcedoff.png', size_hint=(1, None), allow_stretch=False, height=800)
        button_showcurrentenergydata = Button(background_normal='images/showcedoff.png', background_down='images/showcedon.png')
        button_showcurrentenergydata.bind(on_press=lambda x: self.change_image(button_showcurrentenergydata, showcurrentenergydata))
        layout.add_widget(button_showcurrentenergydata)

        return layout

    def change_image(self, button, image):
        if button.background_normal == image.source:
            button.background_normal = button.background_down
        else:
            button.background_normal = image.source

    def change_color(self, widget, color):
        widget.canvas.before.clear()
        widget.canvas.before.add(Color(*color))
        widget.canvas.before.add(Rectangle(size=widget.size, pos=widget.pos))


if __name__ == '__main__':
    Window.clearcolor = (1, 0.9569, 0.7843, 1)
    Window.size = (1200, 1000)
    control().run()
