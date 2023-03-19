import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class Pi(App):
    def build(self):
        fig, ax = plt.subplots(figsize=(10,7))
        fig.set_facecolor("#FFF3C8")
        ax.set_facecolor("#FFF3C8")
        layout = BoxLayout(orientation='vertical')
        energy_distribution = [30, 20, 10, 15, 5, 20]
        labels = ['Refrigerator', 'Washing Machine', 'Heating', 'Lighting', 'Television', 'Other']
        plt.pie(energy_distribution, labels=labels)
        plt.title('Energy Distribution Across Household')
        plt.savefig('pie_chart.png')
        image = Image(source='pie_chart.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(image)
        total_energy = sum(energy_distribution) / 100 * 10
        return layout
Pi().run()
