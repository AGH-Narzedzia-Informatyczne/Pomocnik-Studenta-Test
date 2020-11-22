from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
class CalendarWindow(Screen):
    pass

class GradesWindow(Screen, FloatLayout,GridLayout):
    pass

class SpendingsWindow(Screen):
    pass

class ComparisonWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class ScreenApp(App):
    def build(self):
        return WindowManager()


if __name__ == '__main__':
    ScreenApp().run()