from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd
from kivy.core.window import Window
Success = False
def is_valid(email):
    valid = False
    flag_at = False #checks for @#
    flag_dot = False # checks for.#
    char_before_symbol = False # checks for character before symbol #
    lenemail = False # checks for less than 256 letters#
    letter_between = False #checks num of charcacters between . and @#
    letters_after_dot = False #num of letters after .#
    first_letter = False #first letter is not a symbol#

    strlen= len(email)
    if strlen <= 256:
        lenemail= True
    pos_at=0
    pos_dot=0
    for i in range (0, len(email)):            
        if email[i] == "@":
            flag_at = True
            pos_at= i         
        
        elif email[i] == ".":
            flag_dot = True
            pos_dot= i
               
    if pos_at >1:
        char_before_symbol = True


    if (pos_dot - pos_at) >0 :
        letter_between = True

    len_dot_diff = len(email) - pos_dot

    if  len_dot_diff >0:
        letters_after_dot = True


    if email[0].isalnum:
        first_letter = True

    if flag_at == True  and flag_dot == True and char_before_symbol == True:
        if  letters_after_dot == True and first_letter == True:
            if lenemail == True and letter_between == True:
                    valid= True
                    return valid
            else:
 
                return valid
        else:

            return valid
    else:

        return valid


def popup():
    
        layout = GridLayout(cols = 2, padding = 100)
        closeButton = Button(text = "invalid")
        layout.add_widget(closeButton) 
        popup = Popup(title ='notification',
                      content = layout, )  
        popup.open()   
        closeButton.bind(on_press = popup.dismiss)



# function that displays the content
def alert():
    show = Pop2()
    window = Popup(title = "ALERT", content = show,
                   size_hint = (None, None), size = (300, 300),background_color=[245/255,245/255,220/255,1])
    window.open()

    
# reading all the data stored

info= {'Name':['user1'],
                    'Email':['user@email.com'],
                    'Password':['pass']}
dataFrame = pd.DataFrame(info)
#NEED TO ADD THIS LINE OF CODE AFTER TRANSFERRING TO RASPBERRY PI dataFrame.to_csv("C:\MY FOLDER\raspberry pi\modules\login.csv")
users=pd.read_csv('login.csv') 

  
# class to call the popup function
class PopupWindow(Widget):
    def btn(self):
        alert()
  
# class to build GUI for a popup window
class Pop2(FloatLayout):
    pass
  

  
# class to accept user info and validate it
class loginWindow(Screen):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    
    def validate(self):
        # validating if the email already exists 
        if self.email.text not in users['Email'].unique():
            alert()
        else:
            # switching the current screen to display validation result
            self.manager.current = 'success'
            
            # reset TextInput widget
            self.email.text = ""
            self.pwd.text = ""

    def build(self):
        # Create the root widget
        root = Scatter(do_scale=False)
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
            # create a new instance of the main app and run it
            main_app = MainApp()
            main_app.run()
  
  
# class to accept sign up info  
class signupWindow(Screen):
    name2 = ObjectProperty(None)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    def signupbtn(self):
        # creating a DataFrame of the info
        users = pd.DataFrame([[self.name2.text, self.email.text, self.pwd.text]],
                            columns = ['Name', 'Email', 'Password'])
        if self.email.text != "":
            if self.email.text not in users['Email'].unique():
  
                # if email does not exist already then append to the csv file
                # change current screen to log in the user now 
                user.to_csv('login.nuumbers', mode = 'a', header = False, index = False)
                sm.current = 'login'
                self.name2.text = ""
                self.email.text = ""
                self.pwd.text = ""
                #valid = is_valid(self.email.text)
                #if valid ==False:
                 #   popup()

                
        else:
            # if values are empty or invalid show pop up
            alert()
Success == True
      
# class to display validation result
class successWindow(Screen):
    pass

# class for managing screens
class WindowManager(ScreenManager):
    pass

  
# kv file
kv = Builder.load_file('login.kv')
sm = WindowManager()
  

  
# adding screens
sm.add_widget(loginWindow(name='login'))
sm.add_widget(signupWindow(name='signup'))
sm.add_widget(successWindow(name='success'))



  
# class that builds gui
class loginMain(App):
    def build(self):
        Window.clearcolor = (234/255,210/255,168/255,1)
        class SuccessScreen(Screen):

            if Success == True:
                Window.clearcolor = (234/255,210/255,168/255,1)
                
        
            sm = ScreenManager()

        return sm

  
# driver function
if __name__=="__main__":
    loginMain().run()




    
                    
        
        
    


    
    
        
        
                    
    
