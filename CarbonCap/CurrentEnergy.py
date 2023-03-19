import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle , Color

class Energy(App):

    def build(self):
        fig, ax = plt.subplots(figsize=(10,7))
        fig.set_facecolor("#FFF3C8")
        ax.set_facecolor("#FFF3C8")
        layout = BoxLayout(orientation='vertical')
        energy_distribution = [30, 20, 10, 15, 5, 20]
        labels = ['Refrigerator', 'Washing Machine', 'Air Conditioner', 'Lighting', 'Television', 'Other']
        plt.pie(energy_distribution, labels=labels)
        layout.canvas.before.clear()
        layout.canvas.before.add(Color(1, 0.95, 0.78, 1))
        layout.canvas.before.add(Rectangle(pos=layout.pos, size=layout.size))
        plt.title('Energy Distribution Across Household')
        plt.savefig('pie_chart.png')
        image = Image(source='pie_chart.png', allow_stretch=True, keep_ratio=False)
        total_label = Label(text=f'Total Energy Used: 95 kW', size_hint=(1, None), height=80)
        layout.add_widget(total_label)
        layout.add_widget(image)

        return layout

Energy().run()
