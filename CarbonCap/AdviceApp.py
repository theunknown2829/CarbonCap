from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random
import datetime
from kivy.uix.image import Image


ADVICE_DICT = {
    'light': [
        "Unplug appliances when not in use.",
        "Turn off lights when leaving a room.",
        "Use energy-efficient light bulbs.",
        "Install dimmer switches to control the amount of light you use.",
        "Use natural light by opening curtains or blinds during the day.",
        "Replace outdated fixtures with energy-efficient ones.",
        "Use motion sensor lights to reduce energy waste.",
        "Choose lamps and lighting fixtures that direct light where it's needed.",
        "Use task lighting instead of overhead lighting.",
    ],
    'heat': [
        "Lower your thermostat in the winter and raise it in the summer.",
        "Install a programmable thermostat.",
        "Seal air leaks around windows and doors.",
        "Use a space heater instead of heating an entire room.",
        "Insulate your home to prevent heat loss.",
        "Close curtains or blinds at night to keep heat in.",
        "Wear warmer clothes instead of cranking up the heat.",
        "Use draft stoppers to prevent cold air from coming in.",
        "Use a humidifier to add moisture to the air, which can make it feel warmer.",
    ],
    'appliances': [
        "Use a clothesline instead of a dryer.",
        "Wash full loads of laundry and dishes.",
        "Choose energy-efficient appliances.",
        "Use a microwave or toaster oven instead of a regular oven.",
        "Defrost food in the refrigerator instead of using a microwave.",
        "Clean your appliances regularly to ensure they are working efficiently.",
        "Use a slow cooker instead of the oven to cook meals.",
        "Opt for a laptop instead of a desktop computer, as they use less energy.",
        "Unplug electronics when not in use to reduce standby power usage.",
    ],
    'water': [
        "Take shorter showers.",
        "Use a low-flow showerhead.",
        "Fix any leaks.",
        "Use a dishwasher instead of washing dishes by hand.",
        "Scrape dishes instead of rinsing them before putting them in the dishwasher.",
        "Collect and reuse greywater from your shower or washing machine for watering plants.",
        "Use a broom instead of a hose to clean outdoor spaces.",
        "Turn off the tap when brushing your teeth or shaving.",
        "Use a bucket to collect and reuse water for plants instead of using a hose.",
    ],
}

GREETINGS = ['Hi!', 'Hello!', 'Hey there!', 'Greetings!']
FOLLOW_UP = ['What else can I help you with?', 'Is there anything else you would like to know?', 'Do you have any other questions?']

class EnergySaverApp(App):
    def build(self):
        image1 = Image(source='images/Advice.png')
        image2 = Image(source='images/R.png')
        self.advice_label = Label(text="Hi, I'm Energía, your virtual assistant!\n How can I help you save energy today?\n Water, Lighting,Heating or Appliances?", font_size=30, font_name= 'Roboto', halign='center', color=(0, 0, 0, 1), size_hint=(1, None), height=500)
        self.category_input = TextInput(text="",multiline=False, font_size=24, halign='left', size_hint=(1, 0.8), height=40, background_color=(0.713, 0.576, 0.435, 1.0))
        self.category_input.bind(on_text_validate=self.get_advice)
        self.help_label = Label(text='Ask away in the text below!', font_size=24, halign='right', color=(0, 0, 0, 1), size_hint=(1, None), height=100)
        home_button = Image(source='images/home.png', size_hint=(1, 1), size=(100, 50))
        home_button.bind(on_touch_down=self.home)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(image1)
        layout.add_widget(self.advice_label)
        layout.add_widget(image2)
        layout.add_widget(self.help_label)
        layout.add_widget(home_button)
        layout.add_widget(self.category_input)
        return layout


    def home(self, instance, touch):
        from HOMEPAGE_40 import MainApp
        if instance.collide_point(*touch.pos):
            root_widget = App.get_running_app().root
            for widget in root_widget.walk(restrict=True):
                root_widget.remove_widget(widget)
            main_app = MainApp()
            main_app.run()



    TERM_TO_CATEGORY = {
        'lighting': [
            'light',
            'bulbs'],
        'heating': ['heat',],
        'appliances': ['appliances',],
        'water': ['water',]
    }

    def get_advice(self, *args):
        user_input = self.category_input.text.lower()
        if any(greeting in user_input for greeting in ['hi', 'hello', 'hey']):
            self.advice_label.text = random.choice(GREETINGS)
        elif any(greeting in user_input for greeting in ['bye', 'goodbye']):
            self.advice_label.text = "Goodbye!"
            self.category_input.disabled = True
        else:
            category = next((category for category in ADVICE_DICT if category in user_input), None)
            if not category:
                for term, term_category in self.TERM_TO_CATEGORY.items():
                    if term in user_input:
                        category = ADVICE_DICT.get(term_category)
                        break
            if category:
                advice = random.choice(ADVICE_DICT[category])
                self.advice_label.text = f"{category.capitalize()} tip: {advice}"
            else:
                self.advice_label.text = "Sorry, I didn't understand. Please try again."
        self.help_label.text = random.choice(FOLLOW_UP)
        self.category_input.text = ''
    

if __name__ == '__main__':
    Config.set('graphics', 'resizable', False)
    Window.size = (1200, 700)
    Window.clearcolor = (1, 0.9569, 0.7843, 1)
    EnergySaverApp().run()
