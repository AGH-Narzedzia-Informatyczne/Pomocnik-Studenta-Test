from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chromedriver = r"C:\Users\Szymek\Downloads\chromedriver"
chrome_options = Options();
chrome_options.add_argument("--headless")


class CalendarWindow(Screen):
    def __init__(self, **kwargs):
        super(CalendarWindow, self).__init__(**kwargs)
        for i in range(7):
            self.button = Button(text=str(i+1), size_hint=(0.1, 0.15), pos_hint={'x': 0.10 + (i/10), 'y': 0.80})
            self.add_widget(self.button)
        for i in range(7):
            self.button = Button(text=str(i+8), size_hint=(0.1, 0.15), pos_hint={'x': 0.10 + (i/10), 'y': 0.65})
            self.add_widget(self.button)
        for i in range(7):
            self.button = Button(text=str(i+15), size_hint=(0.1, 0.15), pos_hint={'x': 0.10 + (i/10), 'y': 0.50})
            self.add_widget(self.button)
        for i in range(7):
            self.button = Button(text=str(i+22), size_hint=(0.1, 0.15), pos_hint={'x': 0.10 + (i/10), 'y': 0.35})
            self.add_widget(self.button)

class GradesWindow(Screen, FloatLayout,GridLayout):
    def __init__(self, **kwargs):
        super(GradesWindow, self).__init__(**kwargs)

        self.lbl = Label(text="Wprowadz fraze, ktora chcesz wyszukac:", font_size = 20, pos_hint={'center_x': 0.5, 'center_y': 0.9} )
        self.add_widget(self.lbl)
        self.btn = Button(text="Szukaj", size_hint=(.1, .05), pos_hint={'center_x': 0.5, 'center_y': 0.62})
        self.btn.bind(on_press=self.pressed)
        self.add_widget(self.btn)
        self.txt = TextInput(font_size = 20, size_hint_y = None, height = 80, width = 100,  pos_hint={'center_x': 0.5, 'center_y': 0.75})
        self.add_widget(self.txt)

    def pressed(self, instance):
        phrase = self.txt.text
        driver = webdriver.Chrome(chromedriver, options=chrome_options)
        driver.get("https://www.pepper.pl")
        driver.find_element_by_xpath("/html/body/main/div[1]/header[1]/div/div/div[3]/form/div/input").send_keys(phrase)
        driver.find_element_by_xpath("/html/body/main/div[1]/header[1]/div/div/div[3]/form/div/input").send_keys(Keys.ENTER)
        for i in range(1, 6):
            cena = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/section/div[1]/article[" + (str)(i) + "]/div/div[3]/span/span[1]/span").text
            nazwa = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/section/div/article[" + (str)(i) + "]/div/div[3]/strong/a").text
            link = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/section/div/article[" + (str)(i) + "]/div/div[3]/strong/a").get_attribute("href")
            self.lbl1 = Label(text=nazwa, font_size=15,pos_hint={'center_x': 0.5, 'center_y': 0.66-i/10.5})
            self.add_widget(self.lbl1)
            self.lbl2 = Label(text=cena, font_size=13, pos_hint={'center_x': 0.5, 'center_y': 0.64-i/10.5})
            self.add_widget(self.lbl2)
            self.lbl3 = Label(text=link, font_size=13, pos_hint={'center_x': 0.5, 'center_y': 0.62-i/10.5})
            self.add_widget(self.lbl3)
            print("Cena:" + cena)
            print("Link:" + link + "\n")

class SpendingsWindow(Screen):
    pass

class ComparisonWindow(Screen, GridLayout):
    def __init__(self, **kwargs):
        super(ComparisonWindow, self).__init__(**kwargs)
        self.submit = Button(text="Wyszukaj", font_size=40)
        self.submit.bind(on_press=self.pressed)


    def pressed(self, instance):
        print("dziala")

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class ScreenApp(App):
    def build(self):
        return WindowManager()


if __name__ == '__main__':
    ScreenApp().run()