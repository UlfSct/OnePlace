from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextFieldRound
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
import sqlite3
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
import database as db
from userClass import User
from kivy_garden.mapview import MapView, MapMarker, MapLayer, MarkerMapLayer, MapMarkerPopup
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout


db_name = 'oneplace.db'
user = User()


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    text = StringProperty()


class WindowManager(ScreenManager):
    pass


class LogWindow(Screen):
    user = ObjectProperty(user)

    def write_data_in_user(self, data):
        self.user.userID = data['userID']
        self.user.username = data['username']
        self.user.money = data['money']
        self.user.exp = data['exp']
        self.user.update_exp(0)
        for i, val in enumerate([data['plant1'], data['plant2'], data['plant3'], data['plant4']]):
            self.user.plants[i] = val

    def login_user(self, usr, pwd):
        data = db.get_user_from_db(db_name, usr, pwd)
        if data:
            self.write_data_in_user(data)
            MDApp.get_running_app().root.current = 'main'
        else:
            MDApp.get_running_app().root.current = 'failedlog'


class RegWindow(Screen):
    def register_user(self, usr, pwd):
        if db.is_user_exists(db_name, usr):
            MDApp.get_running_app().root.current = 'failedreg'
        else:
            db.add_user_to_db(db_name, usr, pwd)
            MDApp.get_running_app().root.current = 'sucreg'


class MainWindow(Screen):
    user = ObjectProperty(user)
    tasks = []
    map = ObjectProperty(None)
    markers = None

    def build_map(self):
        data = db.get_markers(db_name)
        self.markers = [
            MapMarkerPopup(lat=row['lat'], lon=row['lon'], source='img/map/map-marker.ico') for row in data
        ]
        for mp in self.markers:
            mp.add_widget(MDCard())
            self.map.add_widget(mp)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.tasks = db.get_daily_tasks(db_name, 3)


Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class OnePlaceApp(MDApp):
    user = ObjectProperty(user)

    def on_stop(self):
        db.save_user_data(db_name, self.user)

    def build(self):
        Window.size = (500, 780)
        return Builder.load_file("onePlace.kv")


if __name__ == '__main__':
    OnePlaceApp().run()


