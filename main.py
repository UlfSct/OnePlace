from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextFieldRound


class WindowManager(ScreenManager):
    pass


Config.set('graphics', 'resizable', '0')


class OnePlaceApp(MDApp):
    def build(self):
        return Builder.load_file("onePlace.kv")


if __name__ == '__main__':
    OnePlaceApp().run()
