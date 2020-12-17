from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chromedriver = r"C:\Users\Szymek\Downloads\chromedriver"
chrome_options = Options();
chrome_options.add_argument("--headless")


dictionary = {}
przedmioty = []


class CalendarWindow(Screen):
    def __init__(self, **kwargs):
        super(CalendarWindow, self).__init__(**kwargs)
        for i in range(7):
            self.button = Button(text=str(i+1), size_hint=(0.1, 0.15), pos_hint={'x': 0.15 + (i/10), 'y': 0.75})
            self.add_widget(self.button)
        for i in range(7):
            self.button = Button(text=str(i+8), size_hint=(0.1, 0.15), pos_hint={'x': 0.15 + (i/10), 'y': 0.60})
            self.add_widget(self.button)
        for i in range(7):
            self.button = Button(text=str(i+15), size_hint=(0.1, 0.15), pos_hint={'x': 0.15 + (i/10), 'y': 0.45})
            self.add_widget(self.button)
        for i in range(7):
            self.button = Button(text=str(i+22), size_hint=(0.1, 0.15), pos_hint={'x': 0.15 + (i/10), 'y': 0.30})
            self.add_widget(self.button)

        self.pn = Label(text="Poniedzialek", font_size = 15, pos_hint={'center_x': 0.2, 'center_y': 0.92} )
        self.wt = Label(text="Wtorek", font_size = 15, pos_hint={'center_x': 0.3, 'center_y': 0.92} )
        self.sr = Label(text="Sroda", font_size = 15, pos_hint={'center_x': 0.4, 'center_y': 0.92} )
        self.cz = Label(text="Czwartek", font_size = 15, pos_hint={'center_x': 0.5, 'center_y': 0.92} )
        self.pt = Label(text="Piatek", font_size = 15, pos_hint={'center_x': 0.6, 'center_y': 0.92} )
        self.sb = Label(text="Sobota", font_size = 15, pos_hint={'center_x': 0.7, 'center_y': 0.92} )
        self.nd = Label(text="Niedziela", font_size = 15, pos_hint={'center_x': 0.8, 'center_y': 0.92} )

        self.add_widget(self.pn)
        self.add_widget(self.wt)
        self.add_widget(self.sr)
        self.add_widget(self.cz)
        self.add_widget(self.pt)
        self.add_widget(self.sb)
        self.add_widget(self.nd)
        
        
class GradesWindow(Screen, FloatLayout,GridLayout):

    def __init__(self, **kwargs):
        super(GradesWindow, self).__init__(**kwargs)
        self.dropdown = DropDown()



        self.lbl = Label(text="Dzienniczek ocen", font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.95})
        self.add_widget(self.lbl)

        self.przedmiot = Label(text="Dodaj przedmiot", font_size=15, pos_hint={'center_x': 0.1, 'center_y': 0.85})
        self.add_widget(self.przedmiot)
        self.txt_przedmiot = TextInput(font_size=15, size_hint=(.15, .05), pos_hint={'center_x': 0.25, 'center_y': 0.85})
        self.add_widget(self.txt_przedmiot)
        self.btn_przedmiot = Button(text="Dodaj ", size_hint=(.1, .05), pos_hint={'center_x': 0.25, 'center_y': 0.79})
        self.btn_przedmiot.bind(on_press=self.pressed_add_przedmiot)
        self.add_widget(self.btn_przedmiot)


        self.ocena = Label(text="Dodaj ocene", font_size=15, pos_hint={'center_x': 0.6, 'center_y': 0.85})
        self.add_widget(self.ocena)
        self.txt_ocena = TextInput(font_size=15, size_hint=(.15, .05), pos_hint={'center_x': 0.73, 'center_y': 0.85})
        self.add_widget(self.txt_ocena)
        self.btn_ocena = Button(text="Dodaj ", size_hint=(.1, .05), pos_hint={'center_x': 0.75, 'center_y': 0.79})
        self.btn_ocena.bind(on_press=self.pressed_add_ocene)
        self.add_widget(self.btn_ocena)


        self.mainbutton = Button(text="Przedmioty",size_hint=(.13, .05),pos_hint={'center_x': 0.88, 'center_y': 0.85})
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.add_widget(self.mainbutton)



    def pressed_add_przedmiot(self, instance):
        dictionary.update({str(self.txt_przedmiot.text):[]*0})
        przedmioty.append(self.txt_przedmiot.text)
        print(dictionary)
        self.btn = Button(text='%s' % self.txt_przedmiot.text, size_hint_y=None, height=20)
        self.btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
        self.dropdown.add_widget(self.btn)
        self.printGrades()



    def pressed_add_ocene(self, instance):
        self.ocena = int(self.txt_ocena.text)
        dictionary[str(self.mainbutton.text)].append(self.ocena)
        print(dictionary)

        self.printGrades()




    def printGrades(self):
        j = 0
        for i in przedmioty:
            print(i)
            self.lbl1 = Label(text=str(i), size_hint=(.3, .05),font_size=15, pos_hint={'center_x': 0.3, 'center_y': 0.66 - j / 10.5})
            self.add_widget(self.lbl1)
            self.lbl2 = Button(text=str(dictionary[i]), size_hint=(.3, .05),font_size=13, pos_hint={'center_x': 0.6, 'center_y': 0.66 - j / 10.5})
            self.add_widget(self.lbl2)
            j +=1


class SpendingsWindow(Screen):
    pass

class ComparisonWindow(Screen, GridLayout):
    def __init__(self, **kwargs):
        super(ComparisonWindow, self).__init__(**kwargs)

        self.lbl = Label(text="Wprowadź frazę, ktorą chcesz wyszukać:", font_size = 20, pos_hint={'center_x': 0.5, 'center_y': 0.9} )
        self.add_widget(self.lbl)
        self.btn = Button(text="Szukaj", size_hint=(.1, .05), pos_hint={'center_x': 0.5, 'center_y': 0.62}, background_color = (0, 0, 0, 1))
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

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ScreenApp(App):
    def build(self):
        return WindowManager()

if __name__ == '__main__':
    ScreenApp().run()