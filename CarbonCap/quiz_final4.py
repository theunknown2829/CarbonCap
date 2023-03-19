from collections import Counter
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Window.clearcolor = (1, 0.9569, 0.7843, 1)
Window.size = (1200,700)

class HomeButton(Button):
    pass
class PersonalityQuiz(BoxLayout):
    def __init__(self, questions, options, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"

        self.questions_container = BoxLayout(orientation="vertical")
        self.add_widget(self.questions_container)

        self.current_question = 0
        self.questions = questions
        self.options = options
        self.answers = []
        self.add_start_button()
        
    def add_start_button(self):
        start_button = Button(text="Start Quiz", size_hint=(1, 0.2) ,font_size=88, color=(1,1,1) ,background_color=(182/255, 147/255, 111/255))
        start_button.bind(on_press=self.next_question)
        self.questions_container.add_widget(start_button)

    def next_question(self, instance=None):
        self.questions_container.clear_widgets()
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.questions_container.add_widget(Label(text=question, font_size=48, color=(0, 0, 0)))
            options_grid = GridLayout(cols=2, size_hint=(1, 0.8), spacing=10)

            for option in self.options:
                button = Button(text=option, font_size=38, color=(1, 1, 1) ,background_color=(182/255, 147/255, 111/255))
                button.bind(on_press=self.answer)
                options_grid.add_widget(button)
            self.questions_container.add_widget(options_grid)
        else:
            personality = self.determine_personality()
            personality_container = BoxLayout(orientation="vertical")
            self.questions_container.add_widget(personality_container)
            from personality1 import Personality1
            from personality2 import Personality2
            from personality3 import Personality3
            from personality4 import Personality4

            if personality == 'A':
                personality = Personality1()
                personality.run()

            elif personality == 'B':
                 personality = Personality2()
                 personality.run()

            elif personality == 'C':
                 personality = Personality3()
                 personality.run()

            elif personality == 'D':
                 personality = Personality4()
                 personality.run()
    def answer(self, instance):
        answer = instance.text
        self.answers.append(answer)
        self.current_question += 1
        self.next_question()

    def determine_personality(self):
        answer_counts = Counter(self.answers)
        personality = answer_counts.most_common(1)[0][0]
        return personality

class QuizApp(App):
    def build2(self):
        size = (50, 50)
        pos = (Window.width - size[0], Window.height - size[1])
        home_button = HomeButton(background_normal='home.png', size=size, pos=pos)
        
        return home_button

    def build3(self):
        layout = BoxLayout(orientation='vertical', spacing=50, padding=[40, 300, 800, 40])
        outer_layout = FloatLayout(size=(800, 600))
        image2 = Image(source='backround.png', size_hint=(None, None), size=(1300, 1750))
        outer_layout.add_widget(image2)
        return outer_layout
    
    def build(self):
        questions = [
            """How often do you remember to turn off lights when leaving a room?
a. Almost always
b. Sometimes
c. Rarely 
d. Never""",
            """When you wake up in the morning, what's the first thing you do?
a. Turn on the lights
b. Open the curtains
c. Take a shower
d. Have a coffee​""",
            """Do you prefer to use natural light or artificial light?
a. Natural light
b. Artificial light
c. Both, depending on the situation
d. I don't really have a preference​""",
            """How do you feel about using energy-efficient appliances?
a. I love them! They're better for the environment.
b. I don't really care, as long as they get the job done.
c. I prefer traditional appliances, even if they're not as efficient.
d. I use them sometimes, but I don't think they make a big difference.​""",
            """Do you have a programmable thermostat at home?
a. Yes, and I use it all the time.
b. Yes, but I rarely use it.
c. No, I prefer to manually adjust the temperature.
d. No, I don't know what a programmable thermostat is.​""",
            """Do you try to reduce your energy usage by unplugging electronics when not in use and using power strips?
a. Yes, always
b. Yes, but only sometimes
c. No, I don't think it's necessary
d. No, I don't know how to do that""",
            """How often do you use energy-efficient light bulbs?
a. Always
b. Sometimes
c. Rarely
d. Never​""",
            """Do you turn off your computer and other electronics when not in use?
a. Yes, always
b. Yes, but only sometimes
c. No, I leave them on all the time
d. No, I don't know how to do that""",
            """How often do you wash clothes in cold water?
a. Always
b. Sometimes
c. Rarely
d. Never""",
            """Do you air dry clothes instead of using a dryer?
a. Yes, always
b. Yes, but only sometimes
c. No, I prefer the dryer
d. No, I don't have a clothesline​""",
            """Do you use a dishwasher or wash dishes by hand?
a. Dishwasher
b. Wash dishes by hand
c. Both, depending on the situation
d. I don't have a dishwasher​""",
            """How often do you use a microwave instead of the stove or oven?
a. Almost always
b. Sometimes
c. Rarely
d. Never​""",
            """Do you keep your refrigerator and freezer at the appropriate temperature?
a. Yes, always
b. Yes, but only sometimes
c. No, I don't pay attention to the temperature
d. No, I prefer to keep it cold/freezer full​""",
            """Do you use energy-efficient windows and doors?
a. Yes, always
b. Yes, but only in some rooms
c. No, I prefer traditional windows and doors
d. No, I don't know what energy-efficient windows and doors are​"""
        ]

        options = [
            "A",
            "B",
            "C",
            "D"
        ]

        return PersonalityQuiz(questions, options)



if __name__ == "__main__":
    QuizApp().run()
