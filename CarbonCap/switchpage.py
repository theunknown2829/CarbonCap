from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (1, 0.9569, 0.7843, 1)
Window.size = (1200,700)


class MyApp(App):
    def build(self):



        layout = GridLayout(cols=3, rows=3, row_force_default=True, row_default_height=200)
        for i in range (1):
            empty_widget= Widget()
            layout.add_widget(empty_widget)
        title = Image(source='images/switches.png',size_hint=(1, None), allow_stretch=True, height=300)
        layout.add_widget(title)
        for i in range (1):
            empty_widget= Widget()
            layout.add_widget(empty_widget)

        bedoff = Image(source='images/bedoff.png',size_hint=(1, None), allow_stretch=True, height=200)
        layout.add_widget(bedoff)
        bathoff = Image(source='images/bathoff.png',size_hint=(1, None), allow_stretch=True, height=200)
        layout.add_widget(bathoff)
        for i in range (1):
            empty_widget= Widget()
            layout.add_widget(empty_widget)
        longoff = Image(source='images/longoff.png',size_hint=(1, None), allow_stretch=True, height=200)
        layout.add_widget(longoff)
        kitchenoff = Image(source='images/kitchenoff.png',size_hint=(1, None), allow_stretch=True, height=200)
        layout.add_widget(kitchenoff)

        return layout

if __name__ == '__main__':
    MyApp().run()

