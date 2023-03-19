import pandas as pd
import numpy as np
import calendar
import datetime
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.scatter import Scatter
def preds():
    def predict_energy_usage(data_file_path, month_name, temperaturec):
        def linear_regression(X, y):
            X = np.hstack((np.ones((X.shape[0], 1)), X))
            theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
            return theta
        data = pd.read_csv(data_file_path)
        if month_name.capitalize() not in data['Month'].unique() or temperaturec < -10 or temperaturec > 50:
            return None

        month_data = data[data['Month'] == month_name.capitalize()]

        energy_adj = 1
        if temperaturec > 20:
            energy_adj = 1.1
        elif temperaturec < 7:
            energy_adj = 1.2
        else:
            energy_adj = 0.8

        season_adj = 1
        if month_name.capitalize() in ["November", "December", "January", "February"]:
            season_adj = 1.2
        elif month_name.capitalize() in ["September", "October"]:
            season_adj = 1.1

        X = month_data['Temperature(C)'].values.reshape(-1, 1)
        y = month_data['Energy'].values.reshape(-1, 1)
        y = y * energy_adj * season_adj

        theta = linear_regression(X, y)

        temperaturef = temperaturec * 9/5 + 32
        prediction = theta[0][0] + theta[1][0] * temperaturef * energy_adj * season_adj

        draw_graph(data, prediction, month_name.capitalize())
        
        return prediction

    def draw_graph(data, prediction, month_name):

        def draw_bar_graph(data, prediction, month_name):
            fig, ax = plt.subplots(figsize=(29,18))
            fig.set_facecolor("#FFF3C8")
            ax.set_facecolor("#FFF3C8")
            ax.set_title("Energy usage by month", fontsize=36)
            ax.set_xlabel("Month", fontsize=26)
            ax.set_ylabel("Energy (kWh)", fontsize=26)
            
            if prediction is None:
                ax.text(0.5, 0.5, "Invalid input for month or temperature.",
                        horizontalalignment='center', verticalalignment='center',
                        transform=ax.transAxes, fontsize=26)
                ax.set_ylim(0, np.max(data["Energy"].values.tolist()))
            else:
                monthly_averages = data.groupby('Month')['Energy'].mean()
                months = monthly_averages.index
                month_numbers = [list(calendar.month_name).index(month) for month in months]
                energy_values = monthly_averages.values

                sorted_indices = np.argsort(month_numbers)
                months = [datetime.datetime.strptime(month, '%B').strftime('%b') for month in months]
                months = [months[i] for i in sorted_indices]
                energy_values = [energy_values[i] for i in sorted_indices]

                xticks = months.copy()
                ax.tick_params(axis='y', labelsize=26)
                ax.tick_params(axis='x', labelsize=26)

                xticks.remove(datetime.datetime.strptime(month_name.capitalize(), '%B').strftime('%b')) 
                xticks.append("Prediction({})".format(datetime.datetime.strptime(month_name.capitalize(), '%B').strftime('%b')))

                ax.bar(months, energy_values, color='blue')
                ax.bar(datetime.datetime.strptime(month_name.capitalize(), '%B').strftime('%b'), energy_values[months == datetime.datetime.strptime(month_name.capitalize(), '%B').strftime('%b')], color='green') # abbreviate user-inputted month name
                ax.bar("PreD({})".format(datetime.datetime.strptime(month_name.capitalize(), '%B').strftime('%b')), prediction, color='red') # abbreviate user-inputted month name

                ax.set_xticks(xticks)
                ax.legend(['Average Energy', 'Energy({})'.format(datetime.datetime.strptime(month_name.capitalize(), '%B').strftime('%b')), 'Prediction({})'.format(datetime.datetime.strptime(month_name.capitalize(), '%B').strftime('%b'))], fontsize=28)

            fig.savefig('my_plot.png')

        Window.clearcolor = (1, 0.9569, 0.7843, 1)
        Config.set('graphics', 'resizable', False)
        Window.size = (1200,700)
        draw_bar_graph(data, prediction, month_name)

        class MyGraphApp(App):
            def build(self):
                root = Scatter(do_scale=False)
                data = pd.read_csv("energy_data.csv") 
                draw_bar_graph(data, prediction, month_name)
                layout = BoxLayout(orientation='vertical')
                img = Image(source='my_plot.png')
                layout.add_widget(img)
                
                home_button = Button(background_normal='images/home.png', size_hint=(0.12, 0.22), pos_hint={'right': 0.12})
                home_button.bind(on_touch_down=self.home)
                layout.add_widget(home_button)
                return layout

            def home(self, instance, touch):
                from HOMEPAGE_40 import MainApp
                if instance.collide_point(*touch.pos):
                    root_widget = App.get_running_app().root
                    for widget in root_widget.walk(restrict=True):
                        root_widget.remove_widget(widget)
                    main_app = MainApp()
                    main_app.run()
                
            
        if __name__ == '__main__':
            MyGraphApp().run()

    class EnergyWindow(Screen):
        current_temp = ObjectProperty(None)
        prediction_month = ObjectProperty(None)
        
        def predict(self):
            current_temp = self.current_temp.text
            prediction_month = self.prediction_month.text.lower()  
            try:
                temperaturec = int(current_temp)
            except ValueError:
                popup = Popup(title='Error', content=Label(text='Please enter a valid temperature'),
                              size_hint=(None, None), size=(400, 200))
                popup.open()
                return
            valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 
                            'july', 'august', 'september', 'october', 'november', 'december']
            if prediction_month not in valid_months:
                popup = Popup(title='Error', content=Label(text='Please select a valid month'),
                              size_hint=(None, None), size=(400, 200))
                popup.open()
                return

            data_file_path = 'energy_data.csv'
            month_name = prediction_month.capitalize()
            current_temp = int(self.current_temp.text)
            temperaturec = current_temp
            prediction = predict_energy_usage(data_file_path, month_name, temperaturec)
            
    class WindowManager(ScreenManager):
        pass

    class EnergyApp(App):
        def build(self):
            Window.clearcolor = (255/255,243/255,200/255,1)
            layout = FloatLayout(size=(Window.width, Window.height))
            header_image = Image(source='images/Prediction.png',
                                 size_hint=(1, 0.4),
                                 pos_hint={'top': 1})
            layout.add_widget(header_image)
            layout.add_widget(EnergyWindow(name='energy'))
            sm = WindowManager()
            screen = Screen(name='main')
            screen.add_widget(layout)
            sm.add_widget(screen)
            
            return sm

    if __name__=="__main__":
        EnergyApp().run()

preds()




