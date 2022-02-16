from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from math import floor, sqrt


class User(Widget):
    userID = 0
    username = StringProperty('Undefined')
    money = NumericProperty(0)
    exp = NumericProperty(0)
    level = NumericProperty(0)
    plants = [0 for i in range(4)]

    def update_money(self, n):
        self.money += n

    def update_exp(self, n):
        self.exp += n
        self.level = floor((25 + sqrt(625 + 100 * self.exp)) / 50)

    def update_plant(self, n):
        self.plants[n-1] = 1
