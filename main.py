from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
import sqlite3


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    text = StringProperty()


class WindowManager(ScreenManager):
    pass


class LogWindow(Screen):
    def verify(self, db, username, password):
        isOK = False
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        usr = cur.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        if usr and usr['password'] == password:
            isOK = True
        conn.close()
        return isOK

    def login_user(self, usr, pwd):
        if self.verify('oneplace.db', usr, pwd):
            MDApp.get_running_app().root.current = 'main'
        else:
            MDApp.get_running_app().root.current = 'failedlog'


class RegWindow(Screen):
    def check(self, db, username):
        isOK = True
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        usr = cur.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        if usr:
            isOK = False
        conn.close()
        return isOK

    def register_user(self, usr, pwd):
        if self.check('oneplace.db', usr):
            conn = sqlite3.connect('oneplace.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (usr, pwd))
            cur.execute("INSERT INTO userData (userID) VALUES (?)", str(cur.lastrowid))
            conn.commit()
            cur.close()
            conn.close()
            MDApp.get_running_app().root.current = 'sucreg'
        else:
            MDApp.get_running_app().root.current = 'failedreg'


Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class OnePlaceApp(MDApp):
    def build(self):
        Window.size = (500, 780)
        return Builder.load_file("onePlace.kv")


if __name__ == '__main__':
    OnePlaceApp().run()
